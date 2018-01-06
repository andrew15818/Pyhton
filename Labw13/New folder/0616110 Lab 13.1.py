import facebook
import json
graph = facebook.GraphAPI(access_token='EAACEdEose0cBAPOWcK4rrniwCZCD3O2L7FxtWNdsxgyTw3JHJd7Dr3x5BDEP9raWLwNSu0CMIqZCh0nE4cZBw0lEiJExANNyklIu5nqqT7SMi09Q5ZAQZBgIzZBlrEwEB1BRmkhGZBmb8rJwmwJ8iB0W6qcG9OwSKVZAmSoSv2AEBvGI2eKW92jYvYukGfM1ItavxZABAdGkZCXAZDZD', version='2.7')

#post = graph.get_object('10204569587018267'+'_'+'145634995501895', fields= 'id, from')
print()
post = graph.get_objects('')
print('Name: ', post['name'])
print('ID: ', post['id'])
#print(post['id'])
#graph.get_object(id = 'me', fields = 'id')