import csv
import sys

def main():
    check_command_line_argv()
    output = []
    try:
        with open(sys.argv[1],'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                split_name = row['name'].split(',')
                output.append({'first':split_name[1].lstrip(), 'last': split_name[0],'house':row['house']})
        
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')
    with open(sys.argv[2],'w') as file:
        writer = csv.DictWriter(file,fieldnames=['first','last','house'])
        writer.writerow({'first':'first','last':'last','house':'house'})
        for row in output:
            writer.writerow({'first':row['first'],'last':row['last'],'house':row['house']})
            


def check_command_line_argv():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line argumets')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line argumets')
    if '.csv' not in sys.argv[1] or '.csv' not in sys.argv[2]:
        sys.exit('Not csv file')

if __name__ == '__main__':
    main()