import matplotlib.pyplot as plt 
import sys

def main():
 
  if len(sys.argv) < 2:
    print("one argument is required - [directory name]")
    exit(1)
  else:
    dir_name = sys.argv[1]

  delayFile = open(dir_name+"/delay.txt","r")
  last_delays = []
  full_delays = []
  rtx_counts = []
  times = []
  c = 0
  for each in delayFile:
    if c == 0:
      c = 1
      continue
    elif c == 1000:
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

  plt.plot([times[i] for i in range(len(times)) if i % 100 == 0], [full_delays[i] for i in range(len(full_delays)) if i % 100 == 0])
  plt.xlabel('Time (s)')
  plt.ylabel('Full Delays (s)')
  plt.savefig('delay.png')

if __name__ == "__main__":
    main()

