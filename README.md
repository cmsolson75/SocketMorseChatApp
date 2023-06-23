# Socket Morse Chat App

## Description

Socket Morse Chat App is a socket chat application that enables users to send Morse code to each other. It is built using Python and works in a client-server architecture.

## Project Structure

The project consists of three main files:

- `server.py` - Handles the server-side operations like accepting client connections and broadcasting messages.

- `client.py` - Manages the client-side operations, which include connecting to the server, sending and receiving messages.

- `morse.py` - Contains functions to translate and play Morse code sounds based on the messages received.

## Installation

Make sure you have Python installed on your machine. Then, clone this repository to your local machine:

```bash
git clone https://github.com/cmsolson75/SocketMorseChatApp.git
cd socket-morse-chat-app
```

Next, you will need to install the necessary dependencies. This project requires the `playsound` library:

```bash
pip install playsound
```

## Usage

### Running the Server

To start the server, run:

```bash
python server.py
```

This will start a server listening on IP "0.0.0.0" and port 12345.

### Running the Client

To connect to the server as a client, run:

```bash
python client.py
```

When prompted, enter a username. The client will then connect to the server on IP "127.0.0.1" and port 12345.

