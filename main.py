from intils import load_operation, get_filtered_operation, get_last_operation, get_formatted_date, \
     get_hidden_num_check_and_cart, get_description, get_amount, get_currency, get_to_list


def main():

    data = load_operation()
    data_fil = get_filtered_operation(data)
    data_last = get_last_operation(data_fil)
    data_form = get_formatted_date(data_last)
    desc = get_description(data_last)
    amo = get_amount(data_last)
    cur = get_currency(data_last)
    list_to, list_from = get_to_list(data_last)
    to = get_hidden_num_check_and_cart(list_to)
    from_ = get_hidden_num_check_and_cart(list_from)

    for i in range(5):
        print(f'{data_form[i]} {desc[i]}\n{from_[i]} -> {to[i]}\n {amo[i]} {cur[i]}')


if __name__ == '__main__':
    main()
