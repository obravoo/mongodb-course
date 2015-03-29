#El ejemplo de hello world, si se pone localhost
#No se habilita el puerto hacia el exterior.
#Si se habilita si se usa la ip o un dominio

from bottle import route, run, template

@route('/hello/:name')
def index(name='World'):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='172.16.211.129', port=80, debug=True)
