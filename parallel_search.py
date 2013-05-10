#!/usr/bin/python

from joblib import delayed, Parallel
import time
import hashlib

hashes_per_job = 10000
min_job = 0
max_job = 2**32 / hashes_per_job


def verify(job_number):
	nonce_start = job_number * hashes_per_job
	nonce_end = nonce_start + hashes_per_job

	nonce = -1

	# redo the calculations locally here (using the python miner) to find the
	# right nonce

	return nonce


def dispatch(job_number):
	nonce_start = job_number * hashes_per_job
	nonce_end = nonce_start + hashes_per_job

	# generate the PS
  #load the PS file into memory
  ps = open('sha256.ps', 'r')
  source = ps.read()
  ps.close()
  
  #fill out the block header
  bversion = 0
  hashPrevBlock = hashlib.sha256('hashPrevBlock').hexdigest()
  hashMerkleRoot = hashlib.sha256('hashMerkleRoot').hexdigest()
  t = int(time.time())
  bits = 0
  
  #modify the PS source to have the proper block header  
  final_source = source[:source.find('/bversion 0 def')]
  final_source += '/bversion ' + str(bversion) + ' def\n'
  final_source += '/hashPrevBlock 8 array def\n'
  final_source += '/hashMerkleRoot 8 array def\n'
  for x in xrange(8):
    prev_block = int(hashPrevBlock[x*4:(x+1)*4],16)
    merkle_root = int(hashMerkleRoot[x*4:(x+1)*4],16)
    final_source += 'hashPrevBlock ' + str(x) + ' ' + str(prev_block) + ' put\n'
    final_source += 'hashMerkleRoot ' + str(x) + ' ' + str(merkle_root) + ' put\n'
  final_source += '/time ' + str(t) + ' def\n'
  final_source += '/bits ' + str(bits) ' def\n'
  final_source += source[source.find('/nonce_bin 0 def'):]
  
  
	# send it to the printer
  
  
	# wait for response

	if promising_result:
		return True
	else:
		return False

# parallel out
results = Parallel(n_jobs=10)(delayed(dispatch)(i) for i in xrange(max_job))

# verify the promising results
for i in [ n for n,v in enumerate(results) if v == True ]:
	n = verify(i)
	if n != -1:
		print "NONCE FOUND: ", n
