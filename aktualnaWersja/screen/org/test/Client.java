package org.test;

import android.util.Log;
import android.widget.Toast;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintStream;
import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;
import java.util.ArrayList;
import java.util.Enumeration;


public class Client {
    ServerSocket serverSocket;
    String message = "";
    private static final String TAG = "BicomClient";
    static final int socketServerPORT = 8080;
    Socket socket;
    private ArrayList<String> messageList;

    public Client() {
        messageList = new ArrayList<String>();
        Thread socketServerThread = new Thread(new SocketServerThread());
        socketServerThread.start();
    }

    public void onDestroy() {
        if (serverSocket != null) {
            try {
                serverSocket.close();
            } catch (IOException e) {
                // TODO Auto-generated catch block
                Log.d(TAG, e.getStackTrace().toString());
            }
        }
    }

    private class SocketServerThread extends Thread {
        @Override
        public void run() {
            try {
                serverSocket = new ServerSocket(socketServerPORT);

                while (true) {
                    socket = serverSocket.accept();

                    SocketServerReplyThread socketServerReplyThread = new SocketServerReplyThread(socket);
                    socketServerReplyThread.run();
                }
            } catch (IOException e) {
                // TODO Auto-generated catch block
                Log.d(TAG, e.toString());
            }
        }
    }

    private class SocketServerReplyThread extends Thread {

        private Socket hostThreadSocket;

        SocketServerReplyThread(Socket socket) {
            hostThreadSocket = socket;
        }

        @Override
        public void run() {
            try {
                ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream(
                        1024);
                byte[] buffer = new byte[1024];
                int bytesRead;
                InputStream inputStream = hostThreadSocket.getInputStream();

			/*
             * notice: inputStream.read() will block if no data return
			 */
                while ((bytesRead = inputStream.read(buffer)) != -1) {
                    byteArrayOutputStream.write(buffer, 0, bytesRead);
                    message += byteArrayOutputStream.toString("UTF-8");
                }
                messageList.add(message);
                Log.d(TAG, messageList.toString());
                System.out.println("Otrzymalem wiadomosc: " + message);
                message = "";

            } catch (IOException e) {
                // TODO Auto-generated catch block
                Log.d(TAG, e.toString());
            } finally {
                if (hostThreadSocket != null) {
                    try {
                        hostThreadSocket.close();
                    } catch (IOException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                    }
                }
            }
        }

    }

    public ArrayList<String> getMessageList(){
        return messageList;
    }
}

