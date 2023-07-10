from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help="Mostra 'Olá mundo' na tela",
    type=str,
    metavar='STRING',
    default="Olá mundo",
    nargs="+")
args = parser.parse_args()

if args.basic is None:
    print("Você não passou o valor de basic.")
    print("valor de Basic: ", args.basic)
else:
    print("valor de Basic:", args.basic)
