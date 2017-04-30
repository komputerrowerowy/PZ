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
    private String currentArea = "kujawsko-pomorskie-latest";
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
    
    public void connectInstructions(){
        int index = this.instructionList.size() - 1;
        this.instructionList.remove(index);
		for (int i = 0; i < this.instructionList2.size(); i++) {
			Instruction instruction = this.instructionList2.get(i);
			this.instructionList.add(instruction);
		}
        System.out.println("wypisane instrukcje");
        System.out.println(this.instructionList.toString());
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