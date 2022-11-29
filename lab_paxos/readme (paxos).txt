http://rus-linux.net/MyLDP/BOOKS/Architecture-Open-Source-Applications/Vol-4/03/03-clustering-02.html
https://www.geeksforgeeks.org/frequent-element-array/

1) Задайте свой main_word.
По дефолту string main_word = "Main";
Сохраните 5 хешей от main_word+0 до main_word+4

2) Отправьте 5 propose-sha запросов
//https://<site>.repl.co/propose-sha/0/1/597c61...
//0 - node_id
//1 - round_number
//sha(node_sha[0]+":"+round_number)

3) Соберите кворум.

4) Отправьте 5 accept-sha запросов.
//https://<site>.repl.co/accept-sha/0/1/<name>/<sha>
//sha(node_sha[0]+":"+round_number+":"+name)

5) Повторите 25 раз весь цикл синхронизации значений.



//////////////////////////////////////////////////////

https://replit.com/@timhuangt/demoflask



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




//////////////////////////////////////////////////////

https://replit.com/@jturtle_/C-Multithreading#main.cpp



//clang++-7 -pthread -std=c++17 -o main main.cpp
#include <iostream>
#include <stdlib.h>
#include <string.h>

using namespace std;

#define uchar unsigned char
#define uint unsigned int

#define DBL_INT_ADD(a,b,c) if (a > 0xffffffff - (c)) ++b; a += c;
#define ROTLEFT(a,b) (((a) << (b)) | ((a) >> (32-(b))))
#define ROTRIGHT(a,b) (((a) >> (b)) | ((a) << (32-(b))))

#define CH(x,y,z) (((x) & (y)) ^ (~(x) & (z)))
#define MAJ(x,y,z) (((x) & (y)) ^ ((x) & (z)) ^ ((y) & (z)))
#define EP0(x) (ROTRIGHT(x,2) ^ ROTRIGHT(x,13) ^ ROTRIGHT(x,22))
#define EP1(x) (ROTRIGHT(x,6) ^ ROTRIGHT(x,11) ^ ROTRIGHT(x,25))
#define SIG0(x) (ROTRIGHT(x,7) ^ ROTRIGHT(x,18) ^ ((x) >> 3))
#define SIG1(x) (ROTRIGHT(x,17) ^ ROTRIGHT(x,19) ^ ((x) >> 10))

typedef struct {
	uchar data[64];
	uint datalen;
	uint bitlen[2];
	uint state[8];
} SHA256_CTX;

uint k[64] = {
	0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
	0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
	0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
	0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
	0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
	0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
	0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
	0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
};

void SHA256Transform(SHA256_CTX *ctx, uchar data[])
{
	uint a, b, c, d, e, f, g, h, i, j, t1, t2, m[64];

	for (i = 0, j = 0; i < 16; ++i, j += 4)
		m[i] = (data[j] << 24) | (data[j + 1] << 16) | (data[j + 2] << 8) | (data[j + 3]);
	for (; i < 64; ++i)
		m[i] = SIG1(m[i - 2]) + m[i - 7] + SIG0(m[i - 15]) + m[i - 16];

	a = ctx->state[0];
	b = ctx->state[1];
	c = ctx->state[2];
	d = ctx->state[3];
	e = ctx->state[4];
	f = ctx->state[5];
	g = ctx->state[6];
	h = ctx->state[7];

	for (i = 0; i < 64; ++i) {
		t1 = h + EP1(e) + CH(e, f, g) + k[i] + m[i];
		t2 = EP0(a) + MAJ(a, b, c);
		h = g;
		g = f;
		f = e;
		e = d + t1;
		d = c;
		c = b;
		b = a;
		a = t1 + t2;
	}

	ctx->state[0] += a;
	ctx->state[1] += b;
	ctx->state[2] += c;
	ctx->state[3] += d;
	ctx->state[4] += e;
	ctx->state[5] += f;
	ctx->state[6] += g;
	ctx->state[7] += h;
}

void SHA256Init(SHA256_CTX *ctx)
{
	ctx->datalen = 0;
	ctx->bitlen[0] = 0;
	ctx->bitlen[1] = 0;
	ctx->state[0] = 0x6a09e667;
	ctx->state[1] = 0xbb67ae85;
	ctx->state[2] = 0x3c6ef372;
	ctx->state[3] = 0xa54ff53a;
	ctx->state[4] = 0x510e527f;
	ctx->state[5] = 0x9b05688c;
	ctx->state[6] = 0x1f83d9ab;
	ctx->state[7] = 0x5be0cd19;
}

void SHA256Update(SHA256_CTX *ctx, uchar data[], uint len)
{
	for (uint i = 0; i < len; ++i) {
		ctx->data[ctx->datalen] = data[i];
		ctx->datalen++;
		if (ctx->datalen == 64) {
			SHA256Transform(ctx, ctx->data);
			DBL_INT_ADD(ctx->bitlen[0], ctx->bitlen[1], 512);
			ctx->datalen = 0;
		}
	}
}

void SHA256Final(SHA256_CTX *ctx, uchar hash[])
{
	uint i = ctx->datalen;

	if (ctx->datalen < 56) {
		ctx->data[i++] = 0x80;

		while (i < 56)
			ctx->data[i++] = 0x00;
	}
	else {
		ctx->data[i++] = 0x80;

		while (i < 64)
			ctx->data[i++] = 0x00;

		SHA256Transform(ctx, ctx->data);
		memset(ctx->data, 0, 56);
	}

	DBL_INT_ADD(ctx->bitlen[0], ctx->bitlen[1], ctx->datalen * 8);
	ctx->data[63] = ctx->bitlen[0];
	ctx->data[62] = ctx->bitlen[0] >> 8;
	ctx->data[61] = ctx->bitlen[0] >> 16;
	ctx->data[60] = ctx->bitlen[0] >> 24;
	ctx->data[59] = ctx->bitlen[1];
	ctx->data[58] = ctx->bitlen[1] >> 8;
	ctx->data[57] = ctx->bitlen[1] >> 16;
	ctx->data[56] = ctx->bitlen[1] >> 24;
	SHA256Transform(ctx, ctx->data);

	for (i = 0; i < 4; ++i) {
		hash[i] = (ctx->state[0] >> (24 - i * 8)) & 0x000000ff;
		hash[i + 4] = (ctx->state[1] >> (24 - i * 8)) & 0x000000ff;
		hash[i + 8] = (ctx->state[2] >> (24 - i * 8)) & 0x000000ff;
		hash[i + 12] = (ctx->state[3] >> (24 - i * 8)) & 0x000000ff;
		hash[i + 16] = (ctx->state[4] >> (24 - i * 8)) & 0x000000ff;
		hash[i + 20] = (ctx->state[5] >> (24 - i * 8)) & 0x000000ff;
		hash[i + 24] = (ctx->state[6] >> (24 - i * 8)) & 0x000000ff;
		hash[i + 28] = (ctx->state[7] >> (24 - i * 8)) & 0x000000ff;
	}
}

string SHA256(string s_curl) {

  int n = s_curl.length();
  char data[n + 1];
  strcpy(data, s_curl.c_str());
  
	int strLen = strlen(data);
	SHA256_CTX ctx;
	unsigned char hash[32];
	string hashStr = "";

	SHA256Init(&ctx);
	SHA256Update(&ctx, (unsigned char*)data, strLen);
	SHA256Final(&ctx, hash);

	char s[3];
	for (int i = 0; i < 32; i++) {
		sprintf(s, "%02x", hash[i]);
		hashStr += s;
	}

	return hashStr;
}

string exec(string s_curl) {

    int n = s_curl.length();
    char cmd[n + 1];
    strcpy(cmd, s_curl.c_str());
  
    char buffer[128];
    string result = "";

    FILE* pipe = popen(cmd, "r");
    if (!pipe) throw runtime_error("popen() failed!");
    try {
        while (fgets(buffer, sizeof buffer, pipe) != NULL) {
            result += buffer;
        }
    } catch (...) {
        pclose(pipe);
        throw;
    }
    pclose(pipe);
    return result;
}

string site = "https://<site>.repl.co/";

int main() {
  string s_curl = exec("curl "+site+"future-block");
  cout<<s_curl<<endl;

  
  string sha = SHA256(s_curl);
  cout<<sha;


  return 0;
}