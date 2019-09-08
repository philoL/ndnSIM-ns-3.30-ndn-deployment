import matplotlib.pyplot as plt 
import sys

def processDelay(fileName):
  delayFile = open(fileName, "r")
  last_delays = []
  full_delays = []
  rtx_counts = []
  times = []
  c = 0
  for each in delayFile:
    if c == 0:
      c = 1
      continue
    elif c == 10000:
      break
    else:
      c += 1
    l = each.split()
    if l[4] == "LastDelay":
      last_delays.append(l[5])
    else:
      times.append(l[0])
      full_delays.append(l[5])
      rtx_counts.append(l[7])

  flt_rate = 300
  plt.figure(1)
  plt.plot([times[i] for i in range(len(times)) if i % flt_rate == 0], [full_delays[i] for i in range(len(full_delays)) if i % flt_rate == 0])
  plt.tight_layout()
  plt.xlabel('time (s)')
  plt.ylabel('full delays (s)')
  plt.savefig('delay.png')

  plt.figure(2)
  plt.plot([times[i] for i in range(len(times)) if i % flt_rate == 0], [full_delays[i] for i in range(len(full_delays)) if i % flt_rate == 0])
  plt.tight_layout()
  plt.xlabel('time (s)')
  plt.ylabel('rtx count')
  plt.savefig('rtx.png')

def processDrop():
  pass

def processThroughput(fileName):
  ratesFile = open(fileName, "r")
  outDatas = []
  times = []
  c = 0
  for each in ratesFile:
    if "N0" in each and "appFace" in each and "OutData" in each:
      c+=1
      l = each.split()
      times.append(l[0])
      outDatas.append(l[6])      

  max_rate = 190
  plt.figure(3)
  plt.plot([times[i] for i in range(len(times)) if i < max_rate], [outDatas[i] for i in range(len(outDatas)) if i < max_rate])
  plt.tight_layout()
  plt.xlabel('time (s)')
  plt.ylabel('Data rates (s)')
  plt.savefig('data_rates.png')

def main():
 
  if len(sys.argv) < 2:
    print("one argument is required - [directory name]")
    exit(1)
  else:
    dir_name = sys.argv[1]
  
  processDelay(dir_name+"delay.txt")
  processThroughput(dir_name+"rates.txt")
  processDrop()

if __name__ == "__main__":
    main()

