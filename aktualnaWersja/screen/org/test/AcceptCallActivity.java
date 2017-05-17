package org.test;

import android.app.Activity;
import android.app.KeyguardManager;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.media.AudioManager;
import android.os.Build;
import android.os.Bundle;
import android.telephony.TelephonyManager;
import android.util.Log;
import android.view.KeyEvent;
import android.view.WindowManager;

import java.io.IOException;
import java.util.logging.Logger;


public class AcceptCallActivity extends Activity {

    private static Logger logger = Logger.getLogger(String.valueOf(AcceptCallActivity.class));

    private static final String MANUFACTURER_HTC = "HTC";

    private KeyguardManager keyguardManager;
    private AudioManager audioManager;
    private CallStateReceiver callStateReceiver;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        keyguardManager = (KeyguardManager) getSystemService(Context.KEYGUARD_SERVICE);
        audioManager = (AudioManager) getSystemService(Context.AUDIO_SERVICE);
    }

    @Override
    protected void onResume() {
        super.onResume();

        registerCallStateReceiver();
        updateWindowFlags();
        acceptCall();
    }

    @Override
    protected void onPause() {
        super.onPause();

        if (callStateReceiver != null) {
            unregisterReceiver(callStateReceiver);
            callStateReceiver = null;
        }
    }

    private void registerCallStateReceiver() {
        callStateReceiver = new CallStateReceiver();
        IntentFilter intentFilter = new IntentFilter();
        intentFilter.addAction(TelephonyManager.ACTION_PHONE_STATE_CHANGED);
        registerReceiver(callStateReceiver, intentFilter);
    }

    private void updateWindowFlags() {
        if (keyguardManager.inKeyguardRestrictedInputMode()) {
            getWindow().addFlags(
                    WindowManager.LayoutParams.FLAG_DISMISS_KEYGUARD |
                            WindowManager.LayoutParams.FLAG_TURN_SCREEN_ON |
                            WindowManager.LayoutParams.FLAG_SHOW_WHEN_LOCKED);
        } else {
            getWindow().clearFlags(
                    WindowManager.LayoutParams.FLAG_DISMISS_KEYGUARD |
                            WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON |
                            WindowManager.LayoutParams.FLAG_SHOW_WHEN_LOCKED);
        }
    }

    private void acceptCall() {

        // for HTC devices we need to broadcast a connected headset
        System.out.println("accept0");
        boolean broadcastConnected = MANUFACTURER_HTC.equalsIgnoreCase(Build.MANUFACTURER)
                && !audioManager.isWiredHeadsetOn();

        System.out.println("accept00");
        if (broadcastConnected) {
            broadcastHeadsetConnected(false);
        }
        System.out.println("accept1");

        try {

            try {
                // logger.debug("execute input keycode headset hook");
                System.out.println("accept2");
                Runtime.getRuntime().exec("input keyevent " +
                        Integer.toString(KeyEvent.KEYCODE_HEADSETHOOK));
                System.out.println("accept3");

            } catch (IOException e) {
                // Runtime.exec(String) had an I/O problem, try to fall back
                //    logger.debug("send keycode headset hook intents");
                System.out.println("accept4");
                String enforcedPerm = "android.permission.CALL_PRIVILEGED";
                Intent btnDown = new Intent(Intent.ACTION_MEDIA_BUTTON).putExtra(
                        Intent.EXTRA_KEY_EVENT, new KeyEvent(KeyEvent.ACTION_DOWN,
                                KeyEvent.KEYCODE_HEADSETHOOK));
                System.out.println("accept5");
                Intent btnUp = new Intent(Intent.ACTION_MEDIA_BUTTON).putExtra(
                        Intent.EXTRA_KEY_EVENT, new KeyEvent(KeyEvent.ACTION_UP,
                                KeyEvent.KEYCODE_HEADSETHOOK));
                System.out.println("accept6");

                sendOrderedBroadcast(btnDown, enforcedPerm);
                System.out.println("accept7");
                sendOrderedBroadcast(btnUp, enforcedPerm);
                System.out.println("accept8");
            }
        } finally {
            if (broadcastConnected) {
                System.out.println("accept9");
                broadcastHeadsetConnected(false);
                System.out.println("accept10");
            }
        }
        
        //Nie jestem pewien czy ma byc zakomentowane czy nie
        
        finish();

    }

    private void broadcastHeadsetConnected(boolean connected) {
        Intent i = new Intent(Intent.ACTION_HEADSET_PLUG);
        i.addFlags(Intent.FLAG_RECEIVER_REGISTERED_ONLY);
        i.putExtra("state", connected ? 1 : 0);
        i.putExtra("name", "mysms");
        try {
            sendOrderedBroadcast(i, null);
        } catch (Exception e) {
            System.out.println("wyjebalo telefon");
            System.out.println(e.toString());
        }
    }

    public class CallStateReceiver extends BroadcastReceiver {
        @Override
        public void onReceive(Context context, Intent intent) {
            finish();

        }
    }
}
