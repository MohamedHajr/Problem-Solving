from typing import Tuple, Union


def do_encode(*,
              string_input: str,
              last_char: str = '',
              last_num: int = 0,
              aggregation_string: str = '') -> Union[Tuple[str, str, int, str], str]:
    if string_input == '':
        return aggregation_string

    if last_char != string_input[0]:
        return do_encode(
            string_input=string_input[1:],
            last_char=string_input[0],
            last_num=1,
            aggregation_string=aggregation_string+string_input[0]
        )
    elif last_char == string_input[0] and last_num == 1:
        return do_encode(
            string_input=string_input[1:],
            last_char=string_input[0],
            last_num=last_num+1,
            aggregation_string=aggregation_string[:-1] +
            str(last_num+1)+string_input[0]
        )
    elif last_char == string_input[0] and last_num > 1:
        return do_encode(
            string_input=string_input[1:],
            last_char=string_input[0],
            last_num=last_num+1,
            aggregation_string=aggregation_string[:-len(str(last_num))-1] +
            str(last_num+1)+string_input[0]
        )
    else:
        print('There is not else :P')
        return aggregation_string
