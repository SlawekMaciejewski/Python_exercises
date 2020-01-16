if __name__ == '__main__':
    lists_name = ['Ania', 'Marek', 'Krzysiek', 'Gosia']
    output = ''
    for name in lists_name:
        """Faktyczne jednak przy każdym obiegu pętli 
        powstaje nowy obiekt a my ustawiamy jedynie 
        zmienną output na ten, który obecnie jest 
        najdłuższy.
        ● Pozostałe, niepotrzebne elementy zajmują 
        miejsce w pamięci co miałoby duże znaczenie 
        gdyby lista zawierała miliony elementów."""
        output += ' ' + name
        print(id(output))
        print(output)
    print(name)
    name = 'ala'
    print(name)

    board = {}
    for row in range(2):
        for col in range(2):
            board[(row, col)] = False
    print(board)


