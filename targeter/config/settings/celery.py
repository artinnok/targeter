broker_url = 'amqp://guest@localhost//'

timezone = 'Europe/Moscow'

accept_content = ['json']
task_serializer = 'json'

result_serializer = 'json'
result_backend = 'rpc://'

imports = ['api.fetch']

task_routes = {
    'fetch': 'fetch',
    'fetch_media': 'fetch'
}
