from flask import Flask
from hashlib import sha256
import random

app = Flask(__name__)
main_word = "Main"
get_256 = lambda x: sha256(x.encode("utf-8")).hexdigest()
all_nodes = list(range(5))
names, cur_blk_num = 'Adams,Baker,Clark,Davis,Evans,Frank,Ghosh,Hills,Irwin,Jones,Klein,Lopez,Mason,Nalty,Ochoa,Patel,Quinn,Reily,Smith,Trott,Usman,Valdo,White,Xiang,Yakub'.split(','), 1
nodes = {i:[cur_blk_num-1, cur_blk_num-1, get_256(main_word+str(i)), names[cur_blk_num-1]] for i in all_nodes}

def make_changes():
  random.shuffle(all_nodes)
  nodes[all_nodes[0]][-1] = names[cur_blk_num]
  nodes[all_nodes[1]][-1] = names[cur_blk_num]
  nodes[all_nodes[2]][-1] = names[cur_blk_num]

make_changes()

@app.route("/")
def hello_world():
  return '<br>'.join(["Node #{} ➡ ({}) {} : {}".format(i, nodes[i][0], nodes[i][1], nodes[i][-1]) for i in nodes])

@app.route('/propose/<int:node_id>/<int:propose_num>', methods=['GET'])
def propose(node_id, propose_num):
  if propose_num > nodes[node_id][0]:
    nodes[node_id][0] = propose_num
    return nodes[node_id][-1]
  return 'Invalid', 403

@app.route('/accept/<int:node_id>/<int:propose_num>/<name>', methods=['GET'])
def accept(node_id, propose_num, name):
  if propose_num == nodes[node_id][0]:
    nodes[node_id][1] = propose_num
    nodes[node_id][-1] = name
    if len(set([str([nodes[node_id][1], nodes[node_id][-1]]) for node_id in nodes])) == 1:
      global cur_blk_num
      if cur_blk_num < 24:
        cur_blk_num += 1
        make_changes()
    return 'Success', 201
  return 'Invalid', 403

print(get_256(nodes[0][2]))
print(get_256(nodes[0][2]+':1'))

@app.route('/propose-sha/<int:node_id>/<int:propose_num>/<sha>', methods=['GET'])
def propose_sha(node_id, propose_num, sha):
  if get_256(nodes[node_id][2]+':'+str(propose_num)) != sha:
    return 'Invalid', 403
  if propose_num > nodes[node_id][0]:
    nodes[node_id][0] = propose_num
    return nodes[node_id][-1]
  return 'Invalid', 403

@app.route('/accept-sha/<int:node_id>/<int:propose_num>/<name>/<sha>', methods=['GET'])
def accept_sha(node_id, propose_num, name, sha):
  if get_256(nodes[node_id][2]+':'+str(propose_num)+':'+name) != sha:
    return 'Invalid', 403
  if propose_num == nodes[node_id][0]:
    nodes[node_id][1] = propose_num
    nodes[node_id][-1] = name
    if len(set([str([nodes[node_id][1], nodes[node_id][-1]]) for node_id in nodes])) == 1:
      global cur_blk_num
      if cur_blk_num < len(names):
        cur_blk_num += 1
        if cur_blk_num < len(names):
          make_changes()
    return 'Success', 201
  return 'Invalid', 403

app.run(host='0.0.0.0')