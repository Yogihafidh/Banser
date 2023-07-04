
def add_income(income_list, income_desc_list):
    print("============ PEMASUKAN ============")
    income = int(input("Masukkan pemasukan : Rp."))
    income_desc = input("Keterangan : ").lower()
    income_list.append(income)
    income_desc_list.append(income_desc)
    print("Pemasukan berhasil ditambahkan!")
    print("=====================================")

def add_expense(expense_list, expense_desc_list):
    print("============ PENGELUARAN ============")
    expense = int(input("Masukkan pengeluaran : Rp."))
    expense_desc = input("Keterangan : ").lower()
    expense_list.append(expense)
    expense_desc_list.append(expense_desc)
    print("Pengeluaran berhasil ditambahkan!")
    print("=====================================")

def bubble_sort(data):
        n = len(data)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]

def sort_view():
        bubble_sort(income_list)
        bubble_sort(expense_list)

        print("============= SORT DATA =============")
        print("Data berhasil diurutkan!")
        print("Pemasukan : ", income_list)
        print("Pengeluaran : ", expense_list)
        print("=====================================")

def linear_search(arr, keyword):
    for i in range(len(arr)):
        if str(arr[i]) == keyword:
            return i
    else:
        return -1

def search():
    print("============= SEARCH DATA =============")
    print("Pilihan")
    print("1. Mencari Pemasukan")
    print("2. Mencari Pengeluaran")
    choice = int(input("Masukan pilihan anda : "))
    if choice == 1:
        print("Daftar keterangan pemasukan :", income_desc_list)
        keyword = input("Masukkan kata kunci sesuai data diatas : ").lower()
        result = linear_search(income_desc_list, keyword)
        if result == -1:
            print("-----------------------------------------------------")
            print("Keyword tidak ditemukan")
            print("-----------------------------------------------------")
        else:
            print("-----------------------------------------------------")
            print("Pemasukan", keyword, "sebesar", "Rp.",income_list[result])
            print("-----------------------------------------------------")
    elif choice == 2:
        print("Daftar keterangan penegeluaran : ", expense_desc_list)
        keyword = input("Masukkan kata kunci sesuai data diatas : ").lower()
        result = linear_search(expense_desc_list, keyword)
        if result == -1:
            print("-----------------------------------------------------")
            print("Keyword tidak ditemukan")
            print("-----------------------------------------------------")
        else:
            print("-----------------------------------------------------")
            print("Pengeluaran", keyword, "sebesar : ", "Rp.",expense_list[result])
            print("-----------------------------------------------------")


def view_data(income_list, income_desc_list, expense_list, expense_desc_list):
    print("====================== VIEW DATA ============================")
    print("Data berhasil Ditampilkan!")
    print("Daftar Pemasukan : ")
    sum_income = sum(income_list)
    sum_expend = sum(expense_list)
    saldo = sum_income - sum_expend

    for i in range(len(income_list)):
        print(i+1,".", income_desc_list[i], ": Rp.", income_list[i])
    print("Daftar Pengeluaran : ")
    for i in range(len(expense_list)):
        print(i+1,".", expense_desc_list[i], ": Rp.", expense_list[i])

    print("")
    print("-----------------------------------------------------------")
    print("Total")
    print("Total Pemasukan : Rp.",sum_income)
    print("Total pengeluaran : Rp.",sum_expend)
    print("Saldo : Rp.", saldo)
    print("===========================================================")


income_list = []
income_desc_list = []
expense_list = []
expense_desc_list = []


while True:
    print("")
    print("=== APLIKASI PENCATAT KEUANGAN ===")
    print("1. Menambahkan Pemasukan")
    print("2. Menambahkan Pengeluaran")
    print("3. Mengurutkan Data")
    print("4. Mencari Data")
    print("5. Melihat Data")
    print("6. Keluar aplikasi")
    choice = int(input("Masukan pilihan : "))
    print("")

    if choice == 1:
        add_income(income_list, income_desc_list)
    elif choice == 2:
        add_expense(expense_list, expense_desc_list)
    elif choice == 3:
        sort_view()
    elif choice == 4:
        search()
    elif choice == 5:
        view_data(income_list, income_desc_list, expense_list, expense_desc_list)
    elif choice == 6:
        break
    else:
        print("Pilihan tidak tersedia, silahkan pilih pilihan lainnya")
