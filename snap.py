import sys,os,snapshothelper
def menu():
 os.system('clear')
 print'''
        1. create the snapshot
        2. list snapshot files
        3. compare snapshots
        4. exit
       '''
 choice=raw_input("\t")
 return choice
choice = ""
while choice != '5':
 choice = menu()
 if choice == '1':
  os.system('clear')
  print '''CREATE SNAPSHOT
===================================='''
  directory = raw_input \
('Enter the directory name to create a snapshot of: ')
  filename = raw_input \
('Enter the name of the snapshot file to create: ')
  snapshothelper.createSnapshot(directory, filename)
 elif choice == '2':
  os.system('clear')
  print '''
        LIST SNAPSHOT FILES
====================================
Enter the file extension for your snapshot files
(for example, 'snp' if your files end in '.snp'):
'''
  extension = raw_input("\t\t")
  snapshothelper.listSnapshots(extension)
 elif choice == '3':
  os.system('cls')
  print '''
COMPARE SNAPSHOTS
====================================
'''
  snap1 = raw_input('Enter the filename of snapshot 1: ')
  snap2 = raw_input('Enter the filename of snapshot 2: ')
  snapshothelper.compareSnapshots(snap1, snap2)
 
 else:
  if choice != '4':
   snapshothelper.invalidChoice() 