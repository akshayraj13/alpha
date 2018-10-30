package com.alacriti.chat;

import java.io.IOException;
import java.util.logging.Logger;

import javax.servlet.ServletException;
import javax.websocket.OnClose;
import javax.websocket.OnMessage;
import javax.websocket.OnOpen;
import javax.websocket.server.ServerEndpoint;

import org.xnio.OptionMap;
import org.xnio.Xnio;
import org.xnio.XnioWorker;

import io.undertow.Handlers;
import io.undertow.Undertow;
import io.undertow.server.handlers.resource.ClassPathResourceManager;
import io.undertow.servlet.api.DeploymentManager;
import io.undertow.websockets.jsr.WebSocketDeploymentInfo;

import static io.undertow.servlet.Servlets.defaultContainer;
import static io.undertow.servlet.Servlets.deployment;
import static io.undertow.websockets.jsr.WebSocketDeploymentInfo.ATTRIBUTE_NAME;


public class App 

{
 /*
	    @ServerEndpoint("/")
	   public static class SocketProxy {

	        @OnOpen
	        public void onOpen() {
	            System.out.println("onOpen");
	        }

	        @OnClose
	        public void onClose() {
	        	System.out.println("onClose");
	        }

	        @OnMessage
	        public void onMessage(String message) {
	        	System.out.println("onMessage:" + message);
	        }

	    }

		public static void main(String[] args) throws ServletException, IOException {
	        final Xnio xnio = Xnio.getInstance("nio", Undertow.class.getClassLoader());
	        final XnioWorker xnioWorker = xnio.createWorker(OptionMap.builder().getMap());
	        final WebSocketDeploymentInfo webSockets = new WebSocketDeploymentInfo()
	                .addEndpoint(SocketProxy.class)
	                .setWorker(xnioWorker);
	        final DeploymentManager deployment = defaultContainer()
	                .addDeployment(deployment()
	                        .setClassLoader(App.class.getClassLoader())
	                        .setContextPath("/")
	                        .setDeploymentName("embedded-websockets")
	                        .addServletContextAttribute(ATTRIBUTE_NAME, webSockets));

	        deployment.deploy();
	        Undertow.builder().
	                addHttpListener(8088, "localhost")
	                .setHandler(deployment.start())
	                .setHandler(Handlers.path().addPrefixPath("/test", Handlers.resource(new ClassPathResourceManager(App.class.getClassLoader(), App.class.getPackage())).addWelcomeFiles("index.html")))
	                .build()
	                .start();

	    }*/

    /*public static void main( String[] args )
    {
    	 int port = 8080;
    	    
    	     *  "localhost" will ONLY listen on local host.
    	     *  If you want the server reachable from the outside you need to set "0.0.0.0"
    	     
    	    String host = "localhost";

    	    
    	     * This web server has a single handler with no routing.
    	     * ALL urls are handled by the helloWorldHandler.
    	     
    	    Undertow server = Undertow.builder()
                    .addHttpListener(8088, "localhost")
                    .setHandler(new HttpHandler() {
                        @Override
                    	public void handleRequest(final HttpServerExchange exchange) throws Exception {
                            exchange.getResponseHeaders().put(Headers.CONTENT_TYPE, "text/plain");
                            exchange.getResponseSender().send("Hello World");
                        }
                    }).build();
    	    System.out.println("starting on http://" + host + ":" + port);
    	    server.start();
    }
    */
	
}
