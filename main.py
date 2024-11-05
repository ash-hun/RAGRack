import yaml
from pyfiglet import Figlet

if __name__ == '__main__':
    #########################
    #    Display Header     #
    #########################
    print("=" * 100)
    t = Figlet(font='slant')
    print(t.renderText('RAG - Rack'))
    print("="*100)


    #########################
    #    Read YAML File     #
    #########################
    with open('config.yaml', 'r') as file:
        config_value = yaml.load(file, yaml.SafeLoader)

    print(config_value)

