broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'US/Mountain'
enable_utc = True

task_routes = {
#'tasks.add': 'low-priority',
}

task_annotations = {
   #'tasks.add': {'rate_limit': '10/m'}
}