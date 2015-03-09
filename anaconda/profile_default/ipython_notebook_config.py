# ipython_notebook_config.py
c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False
c.NotebookApp.base_url = '/ipython/'
c.NotebookApp.webapp_settings = {'static_url_prefix':'/ipython/static/'}
c.NotebookApp.certfile = u'/root/.ipython/profile_default/ipy.pem'
c.NotebookApp.keyfile = u'/root/.ipython/profile_default/ipy.key'
