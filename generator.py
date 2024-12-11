from finetune.utils import tuple2dict, gen_midi
import re
import json


# Input text

# Function to parse the input text
def extract_lines(input_text):
    # Split the input into attempts based on markers
    attempts = re.split(r'------attempt \d+------', input_text)

    results = []  # To store lines for each attempt

    for attempt in attempts[1:]:
        if not attempt.strip():  # Skip empty sections
            continue

        # Find all "The Xth line:" and their associated text
        lines = re.findall(r"(The \w+ line:.*?\n.*?)(?=The \w+ line:|$)", attempt, re.DOTALL)
        # Clean up whitespace and store
        results.append([line.strip() for line in lines])
    return results


if __name__ == '__main__':
    txt = """
    Create a song on brave and sacrificing with a rapid pace.
    ------attempt 0------
    e a song on brave and sacrificing with a rapid pace.[UNUSED_TOKEN_145]
    [UNUSED_TOKEN_146]assistant
    The song is as follows. <bop> Total 5 lines. The first line:to, <A4> , <98> , <79> |give, <A4> , <99> , <79> |you, <A4> , <119> , <127> |the, <A4> , <98> , <79> |love, <A4> , <103> , <79> |that, <A4> , <119> , <79> The second line:to, <A4> , <99> , <79> |give, <A4> , <98> , <79> |you, <A4> , <113> , <79> |the, <A4> , <118> , <79> |love, <G4> , <113> , <79> |that, <F4> , <100> , <79> |i, <G4> , <103> , <79> |feel, <F4> , <153> , <79> The third line:to, <C5> , <103> , <79> |give, <C5> , <118> , <79> |you, <A4> , <98> , <79> |the, <A4> , <96> , <79> |love, <A4> , <125> , <79> |that, <G4> , <126> , <79> The fourth line:love, <E4> , <98> , <79> |i, <G4> , <116> , <79> |need, <E4> , <103> , <79> |is, <F4> , <151> , <79> |the, <G4> , <107> , <79> |love, <A4> , <115> , <79> |we, <G4> , <102> , <79> |share, <F4> , <140> , <167> The fifth line:let, <A4> , <97> , <79> |this, <A4> , <126> , <79> |groove, <G4> , <99> , <79> |light, <A4> , <103> , <79> |up, <F4> , <145> , <79> |your, <G4> , <113> , <79> |fuse, <A4> , <97> , <79> |right, <G4> , <99> , <79> |now, <F4> , <125> , <79> <eop>
    ------attempt 1------
    e a song on brave and sacrificing with a rapid pace.[UNUSED_TOKEN_145]
    [UNUSED_TOKEN_146]assistant
    The song is as follows. <bop> Total 5 lines. The first line:if, <E4> , <116> , <79> |you, <E4> , <148> , <79> |love, <E4> , <116> , <79> |some, <D4> , <116> , <79> |one, <D4> , <116> , <79> |tell, <D4> , <116> , <79> |her, <D4> , <116> , <79> |to, <C4> , <116> , <79> |show, <D4> , <116> , <79> |it, <D4> , <116> , <252> The second line:she, <E4> , <116> , <79> |may, <E4> , <116> , <79> |be, <E4> , <116> , <79> |a, <E4> , <148> , <79> |queen, <E4> , <116> , <79> |by, <D4> , <116> , <79> |day, <D4> , <116> , <79> |but, <D4> , <116> , <79> |at, <D4> , <116> , <252> The third line:just, <E4> , <116> , <79> |so, <E4> , <116> , <79> |you, <D4> , <148> , <79> |got, <C4> , <148> , <79> |to, <D4> , <116> , <79> |love, <D4> , <116> , <79> |your, <E4> , <148> , <79> |self, <D4> , <116> , <79> The fourth line:or, <C4> , <116> , <79> |no, <D4> , <116> , <79> |bod, <D4> , <116> , <79> |y, <D4> , <116> , <79> |else, <C4> , <116> , <79> |wil, <D4> , <116> , <252> |love, <E4> , <116> , <79> |you, <E4> , <116> , <79> The fifth line:oh, <C4> , <116> , <79> |no, <D4> , <116> , <79> |gon, <E4> , <148> , <79> |na, <D4> , <116> , <436> |e, <E4> , <116> , <79> |ven, <D4> , <116> , <79> |pay, <C4> , <116> , <79> |me, <C4> , <148> , <79> |my, <A3> , <201> , <436> <eop>
    ------attempt 2------
    e a song on brave and sacrificing with a rapid pace.[UNUSED_TOKEN_145]
    [UNUSED_TOKEN_146]assistant
    The song is as follows. <bop> Total 5 lines. The first line:这, <A3> , <116> , <79> |条, <B3> , <116> , <79> |路, <C#4> , <151> , <79> |我, <B3> , <151> , <79> |们, <C#4> , <163> , <79> |一, <F#3> , <144> , <79> |起, <C#4> , <175> , <79> |走, <B3> , <141> , <127> The second line:一, <C#4> , <147> , <79> |直, <B3> , <147> , <79> |向, <C#4> , <123> , <79> |前, <B3> , <116> , <79> |走, <C#4> , <144> , <79> |不, <E4> , <130> , <79> |回, <B3> , <175> , <79> |头, <A3> , <160> , <160> The third line:哪, <A3> , <120> , <79> |怕, <F#3> , <120> , <79> |你, <A3> , <154> , <79> |会, <B3> , <137> , <79> |累, <C#4> , <134> , <79> |着, <E4> , <130> , <88> |了, <E4> , <163> , <79> |伤, <C#4> , <147> , <79> |着, <B3> , <166> , <79> The fourth line:不, <A3> , <100> , <79> |会, <A3> , <100> , <79> |怕, <B3> , <151> , <79> |人, <C#4> , <147> , <79> |生, <B3> , <130> , <79> |苦, <C#4> , <172> , <79> |涩, <F#3> , <147> , <79> |的, <B3> , <163> , <79> |酒, <C#4> , <144> , <79> The fifth line:要, <B3> , <151> , <79> |咽, <C#4> , <134> , <79> |下, <B3> , <120> , <79> |去, <C#4> , <123> , <79> |自, <B3> , <116> , <79> |己, <C#4> , <141> , <79> |的, <E4> , <134> , <79> |痛, <B3> , <169> , <79> |楚, <A3> , <169> , <166> <eop>"""

    # Extract lines
    lines_per_attempt = extract_lines(txt)
    print(json.dumps(lines_per_attempt,indent=2))

    print(json.dumps(tuple2dict(lines_per_attempt[0][0]), ensure_ascii=False, indent=2))

    for result in lines_per_attempt:
        print(result)

    gen_midi(lines_per_attempt[0][0])