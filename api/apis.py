import http.client
import urllib
import json

headers = {
            "x-api-key": "6263184cc0c2de409d16",
            "userid": "889",
            "Content-Type": "application/x-www-form-urlencoded"
           }

host = "www.notexponential.com"
url = "/aip2pgaming/api/index.php?"
team_id = "1194"


def get_games():
    """

    :return: a list of dicts with {game_id: info}
    """
    conn = http.client.HTTPConnection(host)
    params = {"type": "myGames"}
    suffix = urllib.parse.urlencode(params)
    new_url = url + suffix
    conn.request("GET", url=new_url, headers=headers)
    response = conn.getresponse()
    data = json.loads(response.read())
    conn.close()
    result = data["myGames"]
    return result


def get_moves(game_id):
    """
    :param game_id: string of game_id
    :return: list of dicts with move info
    """
    conn = http.client.HTTPConnection(host)
    params = {"type": "moves", "gameId": game_id, "count": "10000"}
    suffix = urllib.parse.urlencode(params)
    new_url = url + suffix
    conn.request("GET", url=new_url, headers=headers)
    response = conn.getresponse()
    data = json.loads(response.read())
    conn.close()
    if data["code"] == "OK":
        result = data["moves"]
    else:
        result = []
    return result


def get_board_string(game_id):
    """

    :param game_id: game id
    :return: response
    """
    conn = http.client.HTTPConnection(host)
    params = {"type": "boardString", "gameId": game_id}
    suffix = urllib.parse.urlencode(params)
    new_url = url + suffix
    conn.request("GET", url=new_url, headers=headers)
    response = conn.getresponse()
    data = json.loads(response.read())
    conn.close()
    result = data
    return result


def get_board_map(game_id):
    """

    :param game_id:
    :return: dict as {"x,y": "O", "x1,y1": "X"}
    """
    conn = http.client.HTTPConnection(host)
    params = {"type": "boardMap", "gameId": game_id}
    suffix = urllib.parse.urlencode(params)
    new_url = url + suffix
    conn.request("GET", url=new_url, headers=headers)
    response = conn.getresponse()
    data = json.loads(response.read())
    conn.close()
    if data["output"]:
        result = json.loads(data["output"])
    else:
        result = []
    return result


def make_move(game_id, move):
    """

    :param game_id: string of game_id
    :param move: string "x,y"
    :return:
    """
    conn = http.client.HTTPConnection(host)
    params = {"type": "move", "gameId": game_id, "teamId": team_id, "move": move}
    params_encoded = urllib.parse.urlencode(params)
    conn.request("POST", url=url, headers=headers, body=params_encoded)
    response = conn.getresponse()
    data = json.loads(response.read())
    conn.close()
    if data["code"] == "OK":
        return True
    else:
        return False


if __name__ == '__main__':
    get_games()
    a = get_moves("554")
    get_board_string("32")
    get_board_map("16")
    make_move("32", "5,5")
