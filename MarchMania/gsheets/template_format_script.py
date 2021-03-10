key = "1mrB8_kABHHV13GrKvwvFu3QBrWwtVZvG31t7RdHgjEo"

ws = gc.open_by_key(key).worksheet_by_title('Template')

gsheet_cell_map = {
        "0.1": ('G69', 'G70'), "0.2": ('K69', 'K70'), "0.3": ('O69', 'O70'), "0.4": ('S69', 'S70'),
        "1.1": ('A5', 'A7'), "1.2": ('A9', 'A11'), "1.3": ('A13', 'A15'), "1.4": ('A17', 'A19'), "1.5": ('A21', 'A23'), "1.6": ('A25', 'A27'), "1.7": ('A29', 'A31'), "1.8": ('A33', 'A35'), "1.9": ('A37', 'A39'), "1.10": ('A41', 'A43'), "1.11": ('A45', 'A47'), "1.12": ('A49', 'A51'), "1.13": ('A53', 'A55'), "1.14": ('A57', 'A59'), "1.15": ('A61', 'A63'), "1.16": ('A65', 'A67'), "1.17": ('Y5', 'Y7'), "1.18": ('Y9', 'Y11'), "1.19": ('Y13', 'Y15'), "1.20": ('Y17', 'Y19'), "1.21": ('Y21', 'Y23'), "1.22": ('Y25', 'Y27'), "1.23": ('Y29', 'Y31'), "1.24": ('Y33', 'Y35'), "1.25": ('Y37', 'Y39'), "1.26": ('Y41', 'Y43'), "1.27": ('Y45', 'Y47'), "1.28": ('Y49', 'Y51'), "1.29": ('Y53', 'Y55'), "1.30": ('Y57', 'Y59'), "1.31": ('Y61', 'Y63'), "1.32": ('Y65', 'Y67'),
        "2.1": ('C6', 'C10'), "2.2": ('C14', 'C18'), "2.3": ('C22', 'C26'), "2.4": ('C30', 'C34'), "2.5": ('C38', 'C42'), "2.6": ('C46', 'C50'), "2.7": ('C54', 'C58'), "2.8": ('C62', 'C66'), "2.9": ('W6', 'W10'), "2.10": ('W14', 'W18'), "2.11": ('W22', 'W26'), "2.12": ('W30', 'W34'), "2.13": ('W38', 'W42'), "2.14": ('W46', 'W50'), "2.15": ('W54', 'W58'), "2.16": ('W62', 'W66'),
        "3.1": ('E8', 'E16'), "3.2": ('E24', 'E32'), "3.3": ('E40', 'E48'), "3.4": ('E56', 'E64'), "3.5": ('U8', 'U16'), "3.6": ('U24', 'U32'), "3.7": ('U40', 'U48'), "3.8": ('U56', 'U64'),
        "4.1": ('G12', 'G28'), "4.2": ('G44', 'G60'), "4.3": ('S12', 'S28'), "4.4": ('S44', 'S60'),
        "5.1": ('I20', 'I52'), "5.2": ('Q20', 'Q52'),
        "6.1": ('K35', 'O35')
}
advanced_cell = { # ROUND 0 CHANGES
    "1.1": 'C6', "1.2": 'C10', "1.3": 'C14', "1.4": 'C18', "1.5": 'C22', "1.6": 'C26', "1.7": 'C30', "1.8": 'C34', "1.9": 'C38', "1.10": 'C42', "1.11": 'C46', "1.12": 'C50', "1.13": 'C54', "1.14": 'C58', "1.15": 'C62', "1.16": 'C66', "1.17": 'W6', "1.18": 'W10', "1.19": 'W14', "1.20": 'W18', "1.21": 'W22', "1.22": 'W26', "1.23": 'W30', "1.24": 'W34', "1.25": 'W38', "1.26": 'W42', "1.27": 'W46', "1.28": 'W50', "1.29": 'W54', "1.30": 'W58', "1.31": 'W62', "1.32": 'W66',
    "2.1": 'E8', "2.2": 'E16', "2.3": 'E24', "2.4": 'E32', "2.5": 'E40', "2.6": 'E48', "2.7": 'E56', "2.8": 'E64', "2.9": 'U8', "2.10": 'U16', "2.11": 'U24', "2.12": 'U32', "2.13": 'U40', "2.14": 'U48', "2.15": 'U56', "2.16": 'U64',
    "3.1": 'G12', "3.2": 'G28', "3.3": 'G44', "3.4": 'G60', "3.5": 'S12', "3.6": 'S28', "3.7": 'S44', "3.8": 'S60',
    "4.1": 'I20', "4.2": 'I52', "4.3": 'Q20', "4.4": 'Q52',
    "5.1": 'K35', "5.2": 'O35',
    "6.1": 'M43',
}

for k,v in gsheet_cell_map.items():
    round_num, game_num = map(int, k.split('.'))
  
    N_GAMES =  (2 ** (6-round_num)) if round_num != 0 else 4 # first four

    cell1, cell2 = v
    cell_to_mark1 = right_cell(cell1) if (game_num <= (N_GAMES/2)) else left_cell(cell1)
    cell_to_mark2 = right_cell(cell2) if (game_num <= (N_GAMES/2)) else left_cell(cell2)
    # hacky fix
    if N_GAMES == 1:
        cell_to_mark1 = right_cell(cell1)


    red = {'red':0.9568627450980393, 'green':0.7803921568627451, 'blue':0.7647058823529411 }
    green = {'red':0.7176470588235294, 'green':0.8823529411764706, 'blue':0.803921568627451 }
    yellow = {'red':0.9882352941176471, 'green':0.9098039215686274, 'blue':0.6980392156862745 }
    if round_num == 0:
        condition11 = f"=AND(EXACT({cell_to_mark1},INDIRECT(\"Summary!{cell_to_mark1}\")), EXACT(\".\", {cell_to_mark1}))"
        condition12 = f"=AND(NOT(EXACT({cell_to_mark1},INDIRECT(\"Summary!{cell_to_mark1}\"))), EXACT(\".\", {cell_to_mark1}))"

        
        condition21 = f"=AND(EXACT({cell_to_mark2},INDIRECT(\"Summary!{cell_to_mark2}\")), EXACT(\".\", {cell_to_mark2}))"
        condition22 = f"=AND(NOT(EXACT({cell_to_mark2},INDIRECT(\"Summary!{cell_to_mark2}\"))), EXACT(\".\", {cell_to_mark2}))"

        
    elif round_num != 0:
        to_cell = advanced_cell[k]
        
        condition11 = f"=AND(EXACT(\".\", {cell_to_mark1}), EXACT({to_cell},INDIRECT(\"Summary!{to_cell}\")), NOT(EXACT(\"\",INDIRECT(\"Summary!{to_cell}\"))))"
        condition12 = f"=AND(EXACT(\".\", {cell_to_mark1}), NOT(EXACT({to_cell},INDIRECT(\"Summary!{to_cell}\"))), NOT(EXACT(\"\",INDIRECT(\"Summary!{to_cell}\"))))"

        # condition13 = f"=NOT(EXACT({cell1},INDIRECT(\"Summary!{cell1}\")))"

        condition21 = f"=AND(EXACT(\".\", {cell_to_mark2}), EXACT({to_cell},INDIRECT(\"Summary!{to_cell}\")), NOT(EXACT(\"\",INDIRECT(\"Summary!{to_cell}\"))))"
        condition22 = f"=AND(EXACT(\".\", {cell_to_mark2}), NOT(EXACT({to_cell},INDIRECT(\"Summary!{to_cell}\"))), NOT(EXACT(\"\",INDIRECT(\"Summary!{to_cell}\"))))"
        # condition23 = f"=NOT(EXACT({cell2},INDIRECT(\"Summary!{cell2}\")))"

        
        # condition11 = f"=AND(NOT(EXACT(\"\", INDIRECT(\"Summary!{to_cell}\"))), EXACT({to_cell},INDIRECT(\"Summary!{to_cell}\")), EXACT({cell1}, INDIRECT(\"Summary!{to_cell}\")))"
        # condition12 = f"=AND(NOT(EXACT(\"\", INDIRECT(\"Summary!{to_cell}\"))), NOT(EXACT({to_cell},INDIRECT(\"Summary!{to_cell}\"))), NOT(EXACT({cell1}, INDIRECT(\"Summary!{to_cell}\"))))"

        # condition21 = f"=AND(NOT(EXACT(\"\", INDIRECT(\"Summary!{to_cell}\"))), EXACT({to_cell},INDIRECT(\"Summary!{to_cell}\")), EXACT({cell2}, INDIRECT(\"Summary!{to_cell}\")))"
        # condition22 = f"=AND(NOT(EXACT(\"\", INDIRECT(\"Summary!{to_cell}\"))), NOT(EXACT({to_cell},INDIRECT(\"Summary!{to_cell}\"))), NOT(EXACT({cell2}, INDIRECT(\"Summary!{to_cell}\"))))"

        # ws.add_conditional_formatting(cell1, cell1,'CUSTOM_FORMULA', {'backgroundColor':red}, [condition13])
        # ws.add_conditional_formatting(cell2, cell2,'CUSTOM_FORMULA', {'backgroundColor':red}, [condition23])

    ws.add_conditional_formatting(cell1, cell1,'CUSTOM_FORMULA', {'backgroundColor':green}, [condition11])
    ws.add_conditional_formatting(cell1, cell1,'CUSTOM_FORMULA', {'backgroundColor':red}, [condition12])


    ws.add_conditional_formatting(cell2, cell2,'CUSTOM_FORMULA', {'backgroundColor':green}, [condition21])
    ws.add_conditional_formatting(cell2, cell2,'CUSTOM_FORMULA', {'backgroundColor':red}, [condition22])

# format champ cell
ws.add_conditional_formatting('M43', 'M43','NOT_BLANK', {'backgroundColor':yellow})
