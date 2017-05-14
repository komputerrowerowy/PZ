package org.test;

import android.os.AsyncTask;

import org.json.JSONObject;

import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;

/**
 * Created by zapasowe on 2017-05-04.
 */

public class PostData extends Thread {

    public final static String AUTH_KEY_FCM = "AAAAY2UI7sY:APA91bESLSlQ8X6O1AjzexVGCDbvXIgXaQrxIikyR8J32Q6RDExBp32J_QDL7_ZybWt39cwVxiuurN5HgKWsH3toHXV_5Ti0Hw6z7pDHmrH9Dd0aTKrQ0mt_1tx6cohpKhi1R-EaZ2cN";
    public final static String API_URL_FCM = "https://fcm.googleapis.com/fcm/send";
    JSONObject json;
    String topic;
    
    public PostData(String topic) {
        this.topic = topic;
        json = new JSONObject();
        testMessage();
    }
    public PostData(String topic, JSONObject json) {
        this.topic = topic;
        this.json = json;
    }
    
    @Override
    public void run() {
        try{
            String authKey = AUTH_KEY_FCM;   // You FCM AUTH key
            String FMCurl = API_URL_FCM;
            URL url = new URL(FMCurl);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setUseCaches(false);
            conn.setDoInput(true);
            conn.setDoOutput(true);

            conn.setRequestMethod("POST");
            conn.setRequestProperty("Authorization","key="+authKey);
            conn.setRequestProperty("Content-Type","application/json");
            //testMessage();

            OutputStreamWriter wr = new OutputStreamWriter(conn.getOutputStream());
            wr.write(json.toString());
            wr.flush();
            conn.getInputStream();
            System.out.println("Wiadomosc poszla do: "  + topic);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    private void testMessage(){
        try {
            json.put("to","/topics/" + topic);
            JSONObject info = new JSONObject();
            info.put("title", "Notificatoin Title");   // Notification title
            info.put("body", "Hello Test notification"); // Notification body
            json.put("data", info);
            System.out.println(json.toString());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
