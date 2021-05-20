class Proxy:
    def __init__(self):
        self.client_connection = ClientConnection()
        self.server_connection = ServerConection()
        self.messages = []

    def from_client(self, request):
        self.server_connection.send_to_server(request)
        # adding msg to end of the list
        self.messages.append(request)

    def from_server(self, response):
        self.client_connection.send_to_client(response)

    # own request
    def from_proxy(self, request):
        self.server_connection.send_to_server(request)
        # adding msg to end of the list
        self.messages.append(request)

# TODO add server response parsing
# TODO list is simple solution but can get easily out of hand when
# TODO large portion of data will be send and it will go OOM
# TODO to protect from going OOM list should be cleared from messages that were answered (but index is lost)
# TODO or change list to dict with key as message index

class ServerResponse:
    def __init__(self, sequence_number):
        self.sequence_number = sequence_number


class ClientRequest:
    pass


class ClientConnection:
    def send_to_client(self, server_response):
        return 0


class ServerConection:
    def send_to_server(self, client_request):
        return 0