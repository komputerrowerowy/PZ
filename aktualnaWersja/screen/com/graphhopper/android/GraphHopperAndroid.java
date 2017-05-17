package com.graphhopper.android;

import android.app.Activity;
import android.app.ProgressDialog;
import android.content.Intent;
import android.graphics.Path;
import android.graphics.drawable.Drawable;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.Window;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

//import org.oscim.core.GeoPoint;

import com.graphhopper.GHRequest;
import com.graphhopper.GHResponse;
import com.graphhopper.GraphHopper;
import com.graphhopper.PathWrapper;
import com.graphhopper.util.Constants;
import com.graphhopper.util.Helper;
import com.graphhopper.util.Parameters.Algorithms;
import com.graphhopper.util.Parameters.Routing;
import com.graphhopper.util.PointList;
import com.graphhopper.util.ProgressListener;
import com.graphhopper.util.StopWatch;
import com.graphhopper.util.TranslationMap;
import com.graphhopper.util.Translation;
import com.graphhopper.util.InstructionList;
import com.graphhopper.util.Instruction;
import com.graphhopper.util.PointList;

import java.io.File;
import java.io.FilenameFilter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.Locale;
import com.graphhopper.util.Unzipper;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Date;
import java.text.DateFormat;
import java.util.*;

public class GraphHopperAndroid{
	
	private static final int NEW_MENU_ID = Menu.FIRST + 1;
    private GraphHopper hopper;
    //private GeoPoint start;
    //zprivate GeoPoint end;
    private Spinner localSpinner;
    private Button localButton;
    private Spinner remoteSpinner;
    private Button remoteButton;
    private volatile boolean prepareInProgress = false;
    private volatile boolean shortestPathRunning = false;
    private String currentArea = "poland-latest";
    private String fileListURL = "http://download2.graphhopper.com/public/maps/" + Constants.getMajorVersion() + "/";
    private String prefixURL = fileListURL;
    private String downloadURL;
    private File mapsFolder;
	public PathWrapper resp;
	private Translation tr;
	private final TranslationMap trMap = new TranslationMap().doImport();
	public InstructionList instructionList;
	private Locale locale = new Locale("pl");
    //private ItemizedLayer<MarkerItem> itemizedLayer;
	//private PathLayer pathLayer;
    private InstructionList instructionList2;
    private boolean isCompressed = false;
    private ArrayList<Float> savedPositionListLat;
    private ArrayList<Float> savedPositionListLon;
    private ArrayList<String> savedTimeList;
	
	public GraphHopperAndroid(File mapsFolder){
		System.out.println("graphConstructor");
		boolean greaterOrEqKitkat = Build.VERSION.SDK_INT >= 19;
		if (greaterOrEqKitkat) {
            if (!Environment.getExternalStorageState().equals(Environment.MEDIA_MOUNTED)) {
                System.out.println("GraphHopper is not usable without an external storage!");
                return;
            }
            this.mapsFolder = new File(mapsFolder, "/graphhopper/maps/");
        } else
			this.mapsFolder = new File(mapsFolder, "/graphhopper/maps/");
	
		if (!this.mapsFolder.exists())
			this.mapsFolder.mkdirs();
		
		chooseAreaFromLocal();
        savedPositionListLat = new ArrayList<Float>();
		savedPositionListLon = new ArrayList<Float>();
        savedTimeList = new ArrayList<String>();
	}
    
    public void addActualPosition(float lat, float lon, String datePoint) {
		savedPositionListLat.add(lat);
		savedPositionListLon.add(lon);
        savedTimeList.add(datePoint);
		System.out.println("dodaniePozycji");
		System.out.println(savedPositionListLon.get(savedPositionListLon.size() - 1));
	}
	
	public void saveActualPositionListToGPX(String filePath, String trackName) {
		long startTimeMillis = new Date().getTime();
			
		DateFormat formatter = Helper.createFormatter();
		
		String header = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\" ?>"
                + "<gpx xmlns=\"http://www.topografix.com/GPX/1/1\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\""
                + " creator=\"Graphhopper version " + Constants.VERSION + "\" version=\"1.1\""
                // This xmlns:gh acts only as ID, no valid URL necessary.
                // Use a separate namespace for custom extensions to make basecamp happy.
                + " xmlns:gh=\"https://graphhopper.com/public/schema/gpx/1.1\">"
                + "\n<metadata>"
                + "<copyright author=\"OpenStreetMap contributors\"/>"
                + "<link href=\"http://graphhopper.com\">"
                + "<text>GraphHopper GPX</text>"
                + "</link>"
                + "<time>" + formatter.format(startTimeMillis) + "</time>"
                + "</metadata>";
		StringBuilder gpxOutput = new StringBuilder(header);
		if (savedPositionListLat.size() > 2) {
			createWayPointBlock(gpxOutput, 0, "Start");   // Start 
            createWayPointBlock(gpxOutput, savedPositionListLat.size() - 1, "Koniec!");   // Koniec
			
			
            gpxOutput.append("\n<trk><name>").append(trackName).append("</name>");

            gpxOutput.append("<trkseg>");
            for (int i = 1; i < savedPositionListLat.size() - 1; i++) {
                gpxOutput.append("\n<trkpt lat=\"").append(savedPositionListLat.get(i));
                gpxOutput.append("\" lon=\"").append(savedPositionListLon.get(i)).append("\">");
                long actialTimeMillis = new Date().getTime();
                gpxOutput.append("<time>").append(savedTimeList.get(i)).append("</time>");
                gpxOutput.append("</trkpt>");
            }
            gpxOutput.append("\n</trkseg>");
            gpxOutput.append("\n</trk>");
			
			gpxOutput.append("\n</gpx>");
        
		}
		
		try {
			PrintWriter out = new PrintWriter(filePath);
			out.print(gpxOutput.toString());
			out.close();
		}
		catch (Exception e) {
			System.out.println("jeblo sie");
			System.out.println(e.toString());
		}
	}
	
	private void createWayPointBlock(StringBuilder output, int pointIndex, String name) {
        output.append("\n<wpt ");
        output.append("lat=\"").append(savedPositionListLat.get(pointIndex));
        output.append("\" lon=\"").append(savedPositionListLon.get(pointIndex)).append("\">");

        output.append(" <name>").append(name).append("</name>");
        output.append("</wpt>");
    }
	
	private void chooseAreaFromLocal() {
        List<String> nameList = new ArrayList<String>();
        String[] files = mapsFolder.list(new FilenameFilter() {
            @Override
            public boolean accept(File dir, String filename) {
                return filename != null
                        && (filename.endsWith(".ghz") || filename
                        .endsWith("-gh"));
            }
        });
        Collections.addAll(nameList, files);
        System.out.println("printy printy");
       
        if (nameList.get(0).endsWith(".ghz")){
            isCompressed = true;
            System.out.println(new File(mapsFolder, currentArea).getAbsolutePath() + "-gh" + " " + nameList.get(0));
            File compressed = new File(mapsFolder, nameList.get(0));
            System.out.println(compressed.toString());
            //File compressed = new File(new File(mapsFolder, currentArea).getAbsolutePath() + "-gh" + nameList.get(0));
            unzipFile(compressed, new File(mapsFolder, currentArea).getAbsolutePath() + "-gh", true);
        }
 
        if (nameList.isEmpty())
            return;
 
        /*chooseArea(localButton, localSpinner, nameList,
                new MySpinnerListener() {
                    @Override
                    public void onSelect(String selectedArea, String selectedFile) {
                        initFiles(selectedArea);
                    }
                });*/
    }
   
    private void unzipFile(File compressed, String graphHopperFolder, boolean removeZipped){
        System.out.println("pprinty pprinty");
        try{
            new Unzipper().unzip(compressed.getAbsolutePath(), graphHopperFolder, removeZipped);
        }
        catch(Exception e){
            ;
        }
    }
	
	public void loadGraphStorage() {
        System.out.println("loading graph (" + Constants.VERSION + ") ... ");
		System.out.println("sciezka");
		System.out.println((new File(mapsFolder, currentArea).getAbsolutePath() + "-gh").toString());
		new GHAsyncTask<Void, Void, Path>() {
			protected Path saveDoInBackground(Void... v) throws Exception {
				GraphHopper tmpHopp = new GraphHopper().forMobile();
				tmpHopp.load(new File(mapsFolder, currentArea).getAbsolutePath() + "-gh");
				System.out.println("found graph " + tmpHopp.getGraphHopperStorage().toString() + ", nodes:" + tmpHopp.getGraphHopperStorage().getNodes());
				hopper = tmpHopp;
				return null;
			}

				protected void onPostExecute(Path o) {
					if (hasError()) {
						System.out.println("An error happened while creating graph:"
								+ getErrorMessage());
					} else {
						System.out.println("Finished loading graph. Long press to define where to start and end the route.");
					}

					finishPrepare();
				}
			}.execute();
	}
	
	private void finishPrepare() {
        prepareInProgress = false;
	}
	
    public void calcPath(boolean firstInstructionList, String typeBike,  final double fromLat, final double fromLon,
                         final double toLat, final double toLon) {

        System.out.println("calculating path ...");
            float time;

			StopWatch sw = new StopWatch().start();
			GHRequest req = new GHRequest(fromLat, fromLon, toLat, toLon).
					setAlgorithm(Algorithms.DIJKSTRA_BI);
            // zmiana rodzaju rowerów
			req.setVehicle(typeBike);
			//req.setVehicle("mtb");
			req.getHints().
					put(Routing.INSTRUCTIONS, "true");
			GHResponse resp = hopper.route(req);
			time = sw.stop().getSeconds();
			PathWrapper resp1 = resp.getBest();
			//this.locale = req.getLocale();
			System.out.println("jezyk" + locale.toString());
			this.tr = trMap.getWithFallBack(locale);

			if (!resp1.hasErrors()) {
				System.out.println("from:" + fromLat + "," + fromLon + " to:" + toLat + ","
						+ toLon + " found path with distance:" + resp1.getDistance()
						/ 1000f + ", nodes:" + resp1.getPoints().getSize() + ", time:"
						+ time + " " + resp1.getDebugInfo());
				System.out.println("the route is " + (int) (resp1.getDistance() / 100) / 10f
						+ "km long, time:" + resp1.getTime() / 60000f + "min, debug:" + time);
				System.out.println(resp1.getPoints().toString());
				calcPathResp(resp1, firstInstructionList);
			} else {
				System.out.println("Error:" + resp1.getErrors());
			}
			shortestPathRunning = false;
	}
	
	private void calcPathResp(PathWrapper resp, boolean firstInstructionList) {
		this.resp = resp;
		if (firstInstructionList){
			this.instructionList = resp.getInstructions();
		}
		else{
			this.instructionList2 = resp.getInstructions();
		}
	}
    
    public void connectInstructions() throws FileNotFoundException{
        int index = this.instructionList.size() - 1;
        this.instructionList.remove(index);
		for (int i = 0; i < this.instructionList2.size(); i++) {
			Instruction instruction = this.instructionList2.get(i);
			this.instructionList.add(instruction);
		}
        System.out.println("wypisane instrukcje");
        System.out.println(this.instructionList.toString());
        /*this.instructionList.createGPXList();
        System.out.println(this.instructionList.createGPX());
        
        PrintWriter zapis = new PrintWriter("/sdcard/Bicom/trasa.gpx");
        zapis.println(this.instructionList.createGPX());
        zapis.close();*/
        
  
	}

	
	public String getTurnDescription(int index){
		Instruction instruction = this.instructionList.get(index);
		String turnDescription = instruction.getTurnDescription(this.tr);
		return turnDescription;
	}
	
	public PointList getInstructionPoints(int index){
		Instruction instruction = this.instructionList.get(index);
		PointList points = instruction.getPoints();
		return points;
	}
}
