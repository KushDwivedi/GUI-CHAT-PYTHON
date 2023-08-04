# GUI-CHAT-PYTHON
It's a simple GUI based Real time Chatting portal

# SERVER
Importing Required Libraries
The first three lines of code import the necessary Python libraries which are socket and threading. socket provides low-level network 
functionality, i.e., it helps you create sockets so that you can interface with other machines and the internet. threading module is used to create and manage threads.

Setting up the Server
The next four lines set up the variables for the server. HOST is assigned the value of the IP address of the machine where the server script is running. PORT is assigned an integer value that specifies the port on which the server needs to run. A socket object is created using the socket module to listen to incoming requests. Then the socket options SO_REUSEADDR is set to 1 which ensures that once the server is shut down, the ports are immediately available for use by another server.

Defining Functions
The next four functions include broadcast(), handler(), receiver() which will be called upon while the created threads initialize.
broadcast() is defined to send a message to all of the connected clients.
handler() will keep on receiving messages from the clients and broadcast them to all of the connected clients using the broadcast() function.
receiver() is defined to accept incoming connections from clients and then add them to the list of clients. A new thread will be created for each client which will call the handler() function.

Starting the Server
The last line of the code calls the receiver() function to start the server. Once started, the server will wait for incoming connections. Whenever a new client connects, the server will create a new thread to handle that client.

# RECIVER

Creating a client-side application that can connect to a server over TCP/IP network using sockets. The application uses the tkinter package to create a GUI interface for the client.

The client connects to the specified server HOST and PORT. It initializes a socket object and connects it to the server via the connect() function of the socket module. After that, it shows a UI tiny window to get a name from the user.

A new thread is started for the GUI loop, and another separate thread is started to receive server messages.

The gui_loop() function runs in the GUI thread and creates all the GUI elements, such as labels, text areas, and buttons. It also disables the output textarea so that the user cannot edit it manually. 
The text input area and button are enabled and allow the user to type messages, which are sent to the server when sent with the “Send” button.
The receive() function runs in a separate thread and continuously receives messages from the server. The received messages are then displayed in the GUI text area.
The write() function is called when the user clicks the “Send” button, and it sends the message in the text input area to the server via the send() function of the socket module.

The stop() function is called when the user closes the GUI window, which then closes the connection with the server and terminates the application.
