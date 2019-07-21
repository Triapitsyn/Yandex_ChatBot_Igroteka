import json


class AliceRequest(object):
    def __init__(self, request_dict):
        self._request_dict = request_dict

    @property
    def version(self):
        return self._request_dict['version']

    @property
    def session(self):
        return self._request_dict['session']

    @property
    def user_id(self):
        return self.session['user_id']

    @property
    def is_new_session(self):
        return bool(self.session['new'])
    
    @property
    def command(self):
        return self._request_dict['request']['command']

    @property
    def interfaces(self):
        return self._request_dict['meta']["interfaces"]

    def __str__(self):
        return str(self._request_dict)
    

class AliceResponse(object):
    def __init__(self, alice_request):
        self._response_dict = {
            "version": alice_request.version,
            "session": alice_request.session,
            "response": {
                "end_session": False
            }
        }

    def dumps(self):
        return json.dumps(
            self._response_dict,
            ensure_ascii=False,
            indent=2
        )

    def set_text(self, text):
        self._response_dict['response']['text'] = text[:1024]

    def set_tts(self,text):
        self._response_dict["response"]['tts'] = text[:1024]

    def set_buttons(self, buttons):
        self._response_dict['response']['buttons'] = buttons

    def set_card(self, card):
        self._response_dict["response"]['card'] = card

    def __str__(self):
        return self.dumps()
