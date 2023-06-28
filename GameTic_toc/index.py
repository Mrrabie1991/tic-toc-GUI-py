from PIL import Image, ImageTk  # استفاده از کتابخانه‌ی PIL برای کار با تصاویر

import random  # استفاده از ماژول random برای تولید اعداد تصادفی

# استفاده از کتابخانه‌ی tkinter برای ساخت رابط کاربری
import tkinter as tk

import sys
import subprocess
'''
1. استفاده از کتابخانه‌ی 
`PIL`
 برای کار با تصاویر:
   - این کتابخانه به شما امکان کار با تصاویر در پایتون را می‌دهد.
     با استفاده از 
     `from PIL import Image, ImageTk`
     ،
     کلاس‌ها و توابع مورد نیاز برای کار با تصاویر را وارد می‌کنید.

2. استفاده از ماژول 
`random`:
   - این ماژول برای تولید اعداد تصادفی در پایتون استفاده می‌شود.
     با استفاده از 
     `import random`
     ،
       می‌توانید از توابع تولید اعداد تصادفی آن استفاده کنید.

3. استفاده از کتابخانه‌ی `tkinter` برای ساخت رابط کاربری:
   - این کتابخانه برای ساخت و مدیریت رابط کاربری گرافیکی در پایتون استفاده می‌شود
   . با استفاده از 
   `import tkinter as tk`
   ،
     می‌توانید کلاس‌ها و توابع مورد نیاز برای ساخت پنجره‌ها 
     و المان‌های گرافیکی را وارد کنید.

4. ماژول‌های 
`sys` و `subprocess`:
   - `sys`:
     این ماژول به ارتباط با پایتون وبسایت ها، سیستم عامل، ورژن پایتون 
   و دیگر اطلاعات مربوط به محیط اجرایی پایتون کمک می‌کند.
   - `subprocess`:
     این ماژول به شما امکان اجرای دستورات خط فرمان در پایتون 
   و دریافت خروجی آنها را می‌دهد.

'''



###################################################################
#                                                                 #
#                      Class Menu Gui                             #
#                                                                 #
###################################################################
'''
کلاس 
`MenuGUI`:
   - این کلاس مربوط به ساخت و مدیریت منوی بازی است.
     در این کلاس، یک پنجره اصلی برای نمایش منوی بازی ساخته می‌شود.
   - در این کلاس، متدهای مختلفی مانند 
   `quick_match` 
   و 
   `league`
     وجود دارند که عملکرد منوی بازی ر

ا تنظیم می‌کنند.
   - همچنین، متدهای 
   `get_num_players`
     و 
   `get_player_names`
     برای دریافت تعداد بازیکنان 
   و نام‌های آنها ایجاد شده‌اند.



'''
class MenuGUI:
    def __init__(self):
        self.menu = tk.Tk()  # ایجاد یک شیء از کلاس Tk برای ایجاد پنجره
        self.menu.title('Game Menu')  # تنظیم عنوان پنجره
        self.menu.geometry("500x500")  # تنظیم اندازه پنجره

        self.game_type = ""  # نوع بازی
        self.num_players = 0  # تعداد بازیکنان
        self.player_names = []  # نام‌های بازیکنان

        # ایجاد یک فریم برای دکمه‌ها در پنجره
        menu_frame = tk.Frame(self.menu, bg='gray')
        menu_frame.pack(pady=20)  # قرار دادن فریم در پنجره با فاصله بالا

        quick_match_button = tk.Button(
            menu_frame, text='Quick Match', width=40, height=10, command=self.quick_match)  # ایجاد دکمه "Quick Match"
        # قرار دادن دکمه در فریم با فاصله‌های بالا و چپ
        quick_match_button.pack(pady=50, padx=100)

        league_button = tk.Button(
            menu_frame, text='League', width=40, height=10, command=self.league)  # ایجاد دکمه "League"
        # قرار دادن دکمه در فریم با فاصله‌های بالا و چپ
        league_button.pack(pady=50, padx=100)

    def quick_match(self):
        self.game_type = "Quick Match"  # تنظیم نوع بازی به "Quick Match"
        self.num_players = 2  # تنظیم تعداد بازیکنان به 2
        self.player_names = ['ali', 'Reza']  # تنظیم نام‌های بازیکنان
        self.end()  # بستن پنجره فعلی

    def league(self):
        self.game_type = "League"  # تنظیم نوع بازی به "League"
        self.end()  # بستن پنجره فعلی
        self.get_num_players()  # فراخوانی متد get_num_players

    def get_num_players(self):
        num_players_window = tk.Tk()  # ایجاد یک شیء از کلاس Tk برای ایجاد پنجره جدید
        num_players_window.title("Number of Players")  # تنظیم عنوان پنجره
        num_players_window.geometry("500x500")  # تنظیم اندازه پنجره

        def save_num_players():
            input_value = entry.get()  # دریافت مقدار ورودی از فیلد ورودی

            if input_value.isdigit() and 2 <= int(input_value) <= 8:  # بررسی صحت و اعتبارسنجی مقدار ورودی
                self.num_players = int(input_value)  # تنظیم تعداد بازیکنان
                num_players_window.destroy()  # بستن پنجره
                self.get_player_names()  # فراخوانی متد get_player_names
            else:
                entry.delete(0, tk.END)  # پاک کردن محتوای فیلد ورودی
                entry.insert(0, "Invalid input!")  # نمایش پیام خطا

        entry = tk.Entry(num_players_window)  # ایجاد یک فیلد ورودی در پنجره
        entry.pack(pady=10)  # قرار دادن فیلد ورودی در پنجره با فاصله بالا

        save_button = tk.Button(
            num_players_window, text="Save", command=save_num_players)  # ایجاد دکمه ذخیره
        save_button.pack()  # قرار دادن دکمه در پنجره

        num_players_window.mainloop()  # اجرای حلقه اصلی برنامه برای پنجره num_players_window

    def get_player_names(self):
        player_names_window = tk.Tk()  # ایجاد یک شیء از کلاس Tk برای ایجاد پنجره جدید
        player_names_window.title("Player Names")  # تنظیم عنوان پنجره
        player_names_window.geometry("500x500")  # تنظیم اندازه پنجره

        entry_list = []  # لیستی برای نگهداری فیلدهای ورودی

        def save_player_names():
            # بررسی پر بودن همه فیلدهای ورودی
            all_fields_filled = all(entry.get() for entry in entry_list)

            if all_fields_filled:
                # افزودن مقادیر ورودی به لیست player_names
                self.player_names = [entry.get() for entry in entry_list]
                player_names_window.destroy()  # بستن پنجره

        for i in range(self.num_players):
            entry_label = tk.Label(
                player_names_window, text=f"Player {i+1}:")  # ایجاد برچسب برای هر فیلد ورودی
            entry_label.pack()  # قرار دادن برچسب در پنجره

            # ایجاد یک فیلد ورودی در پنجره
            entry = tk.Entry(player_names_window)
            entry.pack()  # قرار دادن فیلد ورودی در پنجره
            entry_list.append(entry)  # افزودن فیلد ورودی به لیست entry_list

        save_button = tk.Button(
            player_names_window, text="Save", command=save_player_names)  # ایجاد دکمه ذخیره
        save_button.pack()  # قرار دادن دکمه در پنجره

        # اجرای حلقه اصلی برنامه برای پنجره player_names_window
        player_names_window.mainloop()

    def start(self):
        self.menu.mainloop()  # اجرای حلقه اصلی برنامه برای پنجره menu

    def end(self):
        self.menu.destroy()  # بستن پنجره بازی
###################################################################

###################################################################
#                                                                 #
#                      Class Dooz Gui                             #
#                                                                 #
###################################################################
'''
این برنامه یک بازی "دوز" یا "چهارپیوند" 
است که با استفاده از رابط گرافیکی توسط کتابخانه‌ی 
Tkinter
 پیاده‌سازی شده است. بازیکنان می‌توانند نام خود را وارد کرده 
و سپس در صفحه بازی به ترتیب نوبت خودشان دکمه‌ها را انتخاب کنند.
 هدف این بازی برنده شدن با قرار دادن چهار 
 عنصر یکسان (رنگ قرمز یا آبی) در یک خط افقی،
 عمودی یا مورب است. اگر بازیکنی برنده 
 شود یا بازی مساوی شود، پنجره بازی بسته می‌شود.


2
'''

class ConnectFourGame:
    def __init__(self, player1_name, player2_name):

        # ایجاد پنجره اصلی بازی
        self.root = tk.Tk() # ایجاد یک نمونه از کلاس Tk() که پنجره‌ی اصلی برنامه را ایجاد می‌کند
        self.root.title('Dooz')  # تنظیم عنوان پنجره به 'Dooz'

        # تعیین بازیکن‌ها و نتیجه بازی
        self.players = ['r', 'b'] # لیست بازیکن‌ها به صورت رنگ‌های قرمز (r) و آبی (b) تعیین شده است
        self.player1_name = player1_name  # نام بازیکن اول را دریافت و ذخیره می‌کنیم
        self.player2_name = player2_name  # نام بازیکن دوم را دریافت و ذخیره می‌کنیم
        self.result = None  # نتیجه بازی را به ابتدا خالی (None) تعیین می‌کنیم



        # تعریف تصاویر دکمه‌ها و بازیکنان
        # تصاویر مربوط به دکمه‌ها و بازیکنان در بازی با استفاده از نام فایل‌ها تعیین می‌شوند
        self.button_images = {
            'r': 'red.png',    # تصویر مربوط به دکمه قرمز (r)
            'g': 'gray.jpeg',  # تصویر مربوط به دکمه خاکستری (g)
            'b': 'blue.png',   # تصویر مربوط به دکمه آبی (b)
            'but': 'black.jpg'  # تصویر مربوط به دکمه سیاه (but)
        }
        self.player_images = {} # تصاویر مربوط به بازیکنان در بازی را در این دیکشنری ذخیره می‌کنیم


        # بارگیری تصاویر و ذخیره آن‌ها در دیکشنری
        for key, value in self.button_images.items():
            image = ImageTk.PhotoImage(Image.open(
                value).resize((65, 65), Image.LANCZOS)) # بارگیری تصویر مربوطه با استفاده از ImageTk.PhotoImage و Image.open
            self.player_images[key] = image # ذخیره تصویر در دیکشنری self.player_images


        # تعریف صفحه بازی
        # صفحه بازی به صورت یک لیست 2 بعدی از المان‌ها تعریف شده است، که به صورت
        #  'g' (خاکستری) مقداردهی شده‌اند
        self.play_grand = [['g', 'g', 'g', 'g', 'g', 'g', 'g'],
                           ['g', 'g', 'g', 'g', 'g', 'g', 'g'],
                           ['g', 'g', 'g', 'g', 'g', 'g', 'g'],
                           ['g', 'g', 'g', 'g', 'g', 'g', 'g'],
                           ['g', 'g', 'g', 'g', 'g', 'g', 'g'],
                           ['g', 'g', 'g', 'g', 'g', 'g', 'g']]

        # تعریف دکمه‌ها
        # دکمه‌ها به صورت دو لیست جداگانه تعریف شده‌اند

        self.buttons = [] # ای دکمه ها برای نمایش  صفحه بازی ساخته میشن و فانکشنی ندارن
        self.buttons_control = [] # این دمکه برای انخواب ستون بازی هستن و کنترل بازی با این ها هست
        
        # افزودن سطر بالا با نام بازیکنان و رنگ‌هایشان
        # ایجاد یک فریم برای سطر بالا
        top_row = tk.Frame(self.root)
        top_row.pack()

        # ایجاد برچسب مربوط به بازیکن ۱ با نام و رنگ قرمز
        self.player_1_label = tk.Label(
            top_row, text="Player 1: " + self.player1_name, font=('consolas', 14), bg='red')
        self.player_1_label.pack(side=tk.LEFT, padx=10)

        # ایجاد برچسب مربوط به نوبت بازی
        self.turn_label = tk.Label(
            top_row, text="Turn:", font=('consolas', 14))
        self.turn_label.pack(side=tk.LEFT, padx=10)

        # ایجاد برچسب مربوط به بازیکن ۲ با نام و رنگ آبی
        self.player_2_label = tk.Label(
            top_row, text=self.player2_name + ": Player 2", font=('consolas', 14), bg='blue')
        self.player_2_label.pack(side=tk.RIGHT, padx=10)

        # افزودن جداسازی بصری
        # ایجاد یک فریم با ارتفاع ۲۰ پیکسل به عنوان جداسازی
        spacer1 = tk.Frame(self.root, height=20)
        spacer1.pack()


        # ایجاد فریم و دکمه‌های صفحه بازی
        # ایجاد یک فریم برای قرار دادن دکمه‌ها
        frame = tk.Frame(self.root)
        frame.pack()

        # ایجاد دکمه‌های صفحه بازی
        for row, row_data in enumerate(self.play_grand):
            button_row = []
            for col, color in enumerate(row_data):
                # ایجاد دکمه با تصویر مربوطه
                button = tk.Button(frame, image=self.player_images[color])
                # قرار دادن دکمه در شبکه فریم
                button.grid(row=row, column=col)
                # افزودن دکمه به لیست دکمه‌ها
                button_row.append(button)
            # افزودن لیست دکمه‌ها به لیست اصلی دکمه‌ها
            self.buttons.append(button_row)

        # افزودن جداسازی بصری
        # ایجاد یک فریم با ارتفاع ۸ پیکسل به عنوان جداسازی
        spacer = tk.Frame(self.root, height=8)
        spacer.pack()


        # ایجاد یک فریم جدید برای قرار دادن دکمه‌ها در آن
        new_row = tk.Frame(self.root)
        new_row.pack()  # نمایش فریم جدید در رابط کاربری

        for col in range(7):
            button = tk.Button(
                new_row, image=self.player_images['but'], command=lambda col=col: self.next_turn(
                    col)
            )
            button.pack(side=tk.LEFT)  # نمایش دکمه در فریم و چینش آن در سمت چپ
            # افزودن دکمه به لیست self.buttons_control برای کنترل بعدی
            self.buttons_control.append(button)

        # افزودن جداسازی بصری
        # ایجاد یک فریم جدید برای جداسازی بصری (فاصله) بین دکمه‌ها
        spacer0 = tk.Frame(self.root, height=8)
        spacer0.pack()  # نمایش فریم جدید در رابط کاربری

        self.initialize_game()  # فراخوانی تابع initialize_game برای شروع بازی


    def start_game(self):
        self.root.mainloop()  # شروع حلقه اصلی برای اجرای برنامه


    def end_game(self):
        # بستن پنجره بازی
        self.root.destroy()  # نابود کردن پنجره رابط کاربری


    def update_play_grand(self):
        # به روزرسانی صفحه بازی با تصاویر مناسب
        for row, row_buttons in enumerate(self.buttons):
            for col, button in enumerate(row_buttons):
                # دریافت رنگ متناسب با موقعیت فعلی در صفحه بازی
                color = self.play_grand[row][col]
                # تنظیم تصویر متناسب با رنگ بر روی دکمه
                button.configure(image=self.player_images[color])


    def next_turn(self, button_id):
        global player  # استفاده از متغیر گلوبال برای نگهداری بازیکن فعلی

        # یافتن سطر خالی از پایین به بالا
        for row in range(5, -1, -1):
            if self.play_grand[row][button_id] == 'g' and self.check_winner() is False:
                if player == self.players[0]:
                    self.play_grand[row][button_id] = player
                    if self.check_winner() is False:
                        player = self.players[1]
                        self.turn_label.configure(text="Turn: " + self.player2_name,
                                                bg='red' if player == 'r' else 'blue')
                    elif self.check_winner() is True:
                        # بازیکن برنده
                        self.result = self.player1_name if player == self.players[0] else self.player2_name
                        self.turn_label.configure(text=(self.result + " wins"))
                        self.root.after(1500, self.end_game)
                    elif self.check_winner() == "Tie":
                        self.result = "Tie"  # بازی مساوی
                        self.turn_label.configure(text=("Tie!"))
                        self.root.after(1500, self.end_game)
                else:
                    self.play_grand[row][button_id] = player
                    if self.check_winner() is False:
                        player = self.players[0]
                        self.turn_label.configure(text="Turn: " + self.player1_name,
                                                bg='red' if player == 'r' else 'blue')
                    elif self.check_winner() is True:
                        # بازیکن برنده
                        self.result = self.player1_name if player == self.players[0] else self.player2_name
                        self.turn_label.configure(text=(self.result + " wins"))
                        self.root.after(1500, self.end_game)
                    elif self.check_winner() == "Tie":
                        self.result = "Tie"  # بازی مساوی
                        self.turn_label.configure(text=("Tie!"))
                        self.root.after(1500, self.end_game)
                break

        self.update_play_grand()  # به روزرسانی صفحه بازی پس از هر نوبت بازی

    def check_winner(self):
        

        # بررسی چهار پیاپی افقی
        for row in range(6):
            for col in range(4):
                if self.play_grand[row][col] != 'g' and \
                        self.play_grand[row][col] == self.play_grand[row][col + 1] == self.play_grand[row][col + 2] == self.play_grand[row][col + 3]:
                    return True

        # بررسی چهار پیاپی عمودی
        for row in range(3):
            for col in range(7):
                if self.play_grand[row][col] != 'g' and \
                        self.play_grand[row][col] == self.play_grand[row + 1][col] == self.play_grand[row + 2][col] == self.play_grand[row + 3][col]:
                    return True

        # بررسی چهار پیاپی مورب (از چپ به راست)
        for row in range(3):
            for col in range(4):
                if self.play_grand[row][col] != 'g' and \
                        self.play_grand[row][col] == self.play_grand[row + 1][col + 1] == self.play_grand[row + 2][col + 2] == self.play_grand[row + 3][col + 3]:
                    return True

        # بررسی چهار پیاپی مورب (از راست به چپ)
        for row in range(3):
            for col in range(3, 7):
                if self.play_grand[row][col] != 'g' and \
                        self.play_grand[row][col] == self.play_grand[row + 1][col - 1] == self.play_grand[row + 2][col - 2] == self.play_grand[row + 3][col - 3]:
                    return True

        # بررسی اینکه آیا بازی مساوی است
        if all(self.play_grand[0][col] != 'g' for col in range(7)):
            return "Tie"

        return False

    def get_result(self):
        # بازگردانی نتیجه بازی (برنده یا مساوی)
        return self.result

    def initialize_game(self):
        # مقداردهی اولیه بازی
        global player
        player = random.choice(self.players)
        self.turn_label.configure(text="Turn: " + self.player1_name,
                                  bg='red' if player == 'r' else 'blue')

        self.update_play_grand()
####################################################################

###################################################################
#                                                                 #
#                      Class ResultGUI                            #
#                                                                 #
###################################################################
'''
این کد یک کلاس با نام 
`ResultGUI`
 را تعریف می‌کند.
 این کلاس برای نمایش نتیجه‌ی بازی استفاده می‌شود
 . در ابتدای متد 
 `__init__`
   یک پنجره جدید با نام 
 "Game Result"
   ایجاد می‌شود و اندازه 
 آن به 500x500
   پیکسل تنظیم می‌شود.

سپس برچسبی با متن 
"Winner:"
 به اندازه‌ی 24 پیکسل و فونت 
`consolas`
 به پنجره اضافه می‌شود. برچسب برنده نیز با استفاده از متغیر 
 `winner`
   که به عنوان ورودی به کلاس داده می‌شود، ایجاد می‌شود و 
 به پنجره اضافه می‌شود. فونت این برچسب نیز 
 `consolas`
   با اندازه 24 و استایل 
   `bold`
     است.

در ادامه، یک دکمه با متن 
"Restart the program"
 ایجاد می‌شود و متد 
`restart_program`
 به عنوان کالبک آن تعیین می‌شود.
 این متد پنجره نتیجه را بسته 
و برنامه را مجدداً راه‌اندازی می‌کند.

در انتها، متد 
`start`
 برای شروع نمایش پنجره تعریف شده است که تا
 زمانی که پنجره بسته نشده باشد،
 پردازش را به پنجره منتقل می‌کند.
'''

class ResultGUI:
    def __init__(self, winner):
        # ساختن پنجره ی نتیجه بازی
        self.root = tk.Tk()
        self.root.title('Game Result')
        self.root.geometry("500x500")

        # اضافه کردن برچسب برنده
        label = tk.Label(self.root, text="Winner:", font=('consolas', 24))
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        winner_label = tk.Label(self.root, text=winner,
                                font=('consolas', 24, 'bold'))
        winner_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        # اضافه کردن دکمه تنظیم مجدد برنامه
        button = tk.Button(
            self.root, text="Restart the program", command=self.restart_program)
        button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    def restart_program(self):
        # بستن پنجره نتیجه بازی و راه‌اندازی مجدد برنامه
        self.root.destroy()
        python = sys.executable
        subprocess.call([python] + sys.argv)

    def start(self):
        # شروع نمایش پنجره
        self.root.mainloop()







####################################################################


# ایجاد یک نمونه از کلاس MenuGUI
menu = MenuGUI()

# اجرای روش start برای نمونه ایجاد شده
menu.start()

# دسترسی به مقادیر مورد نظر
game_type = menu.game_type
player_count = menu.num_players
player_names = menu.player_names


print("Game Type:", game_type)
print("Player Count:", player_count)
print("Player Names:", player_names)


#####################################################################

###################################################################
#                                                                 #
#                      Fun run_tournament                         #
#                                                                 #
###################################################################

"""
این کد یک تابع با نام 
`run_tournament`
 است که یک لیست از بازیکنان را به 
 عنوان ورودی می‌گیرد و مسابقه‌های تورنمنت را بین 
آن‌ها برگزار می‌کند تا برنده نهایی را تشخیص دهد.

در این تابع، ابتدا لیست بازیکنان را به صورت تصادفی مخلوط می‌کند.
 سپس دو لیست 
 `list1` و `list2`
   را ایجاد می‌کند. 

`list1`
 لیست اصلی بازیکنان است که ترتیب تصادفی دارد و در طول تورنمنت به‌روزرسانی می‌شود. 

`list2` 
لیستی است که برنده‌های هر دوره را دریافت می‌کند.

سپس یک حلقه 
while 
شروع می‌شود تا زمانی که تنها
 یک نفر برنده باقی بماند 
و تعداد بازی‌ها کمتر از 8 باشد. 

در داخل حلقه اصلی،
 ابتدا بازیکن آخر را در صورتی که تعداد بازیکنان فرد باشد
، به لیست برنده‌ها 
(`list2`)
 اضافه می‌کند و سپس دو بازیکن اول را 
 انتخاب کرده و بازی را بین آن‌ها اجرا می‌کند. 

نتیجه بازی را چاپ کرده و در صورتی که بازی مساوی بود
، بازی را مجدداً اجرا کرده و نتیجه را بررسی می‌کند. 

در نهایت، برنده را به لیست برنده‌ها 
(`list2`)
 اضافه می‌کند.

در پایان حلقه 
while،
 لیست 
 `list1`
   را با لیست 
   `list2`
     جایگزین می‌کند و
   لیست 
   `list2`
     را خالی می‌کند. 

سپس شمارنده تعداد بازی‌ها را افزایش می‌دهد.

اگر در نهایت تنها یک بازیکن در لیست 
`list1`
 باقی ماند، او را به عنوان برنده نهایی برگرداند. 

در غیر این صورت، به این معنی
 است که هیچ برنده‌ای وجود ندارد و 
`None`
 را برگرداند.

به طور خلاصه، تابع 
`run_tournament`
 با دریافت لیست بازیکنان، مسابقه‌های تورنمنت را برگزار کرده و برنده نهایی را تشخیص می‌دهد.
"""


def run_tournament(players):
    random.shuffle(players)  # ترتیب بازیکنان را به صورت تصادفی تغییر می‌دهد
    list1 = players  # لیست اصلی بازیکنان که ترتیب تصادفی دارد
    list2 = []  # لیستی برای ذخیره کردن بازیکنان برنده در هر دور
    glist = []  # لیستی برای ذخیره کردن دو بازیکن در هر مسابقه
    cnt = 0  # شمارنده‌ای برای تعداد بازی‌ها

    # تا زمانی که تنها یک نفر برنده باقی نمانده و تعداد بازی‌ها کمتر از 8 باشد
    while len(list1) > 1 and cnt < 8:
        if len(list1) % 2 != 0:  # اگر تعداد بازیکنان فرد باشد
            # بازیکن آخر را به لیست برنده‌ها اضافه می‌کنیم
            list2.append(list1[-1])
            del list1[-1]  # بازیکن آخر را از لیست اصلی حذف می‌کنیم

        while len(list1) > 0:  # تا زمانی که بازیکنانی در لیست اصلی وجود داشته باشد
            glist = list1[:2]  # دو بازیکن اول را در لیست glist ذخیره می‌کنیم
            del list1[:2]  # دو بازیکن اول را از لیست اصلی حذف می‌کنیم

            # چاپ نام دو بازیکن مقابله‌کننده
            print(
                f'A game between {glist[0]} and {glist[1]}')
            # بازی بین دو بازیکن را اجرا کرده و نتیجه را دریافت می‌کنیم
            League = ConnectFourGame(glist[0], glist[1])# ساخت ابجکت بازی از کلاس دوز
            League.start_game()# شروع بازی
            result = League.get_result()# گرفتن نتیجه بازی
            print(f'The result of the game: {result}')  # چاپ نتیجه بازی

            if result == 'Tie':  # اگر بازی مساوی بود
                print('The game is repeated')  # چاپ پیام تکرار بازی
                # مجدداً بازی را اجرا کرده و نتیجه را دریافت می‌کنیم
                League = ConnectFourGame(glist[0], glist[1])# ساخت ابجکت بازی از کلاس دوز
                League.start_game()# اجرای بازی 
                result = League.get_result()# گرفتن نتیجه بازی
                print(f'The result of the game: {result}')  # چاپ نتیجه بازی

                if result == 'Tie':  # اگر بازی مجدداً مساوی بود
                    # یکی از بازیکنان را به صورت تصادفی انتخاب می‌کنیم
                    result = random.choice(glist)
                    # چاپ نتیجه حذف بازیکن
                    print(f'The result of the game is random: {result}')
                    # بازیکن حذف شده را به لیست برنده‌ها اضافه می‌کنیم
                    list2.append(result)
                else:
                    # نتیجه بازی را به لیست برنده‌ها اضافه می‌کنیم
                    list2.append(result)
            else:
                # نتیجه بازی را به لیست برنده‌ها اضافه می‌کنیم
                list2.append(result)

        list1 = list2.copy()  # لیست برنده‌ها را به لیست اصلی می‌کپی کنیم
        list2.clear()  # لیست برنده‌ها را خالی می‌کنیم
        cnt += 1  # شمارنده تعداد بازی‌ها را افزایش می‌دهیم

    if len(list1) > 0:  # اگر بازیکنی در لیست اصلی باقی مانده باشد
        return list1[0]  # آن را به عنوان برنده نهایی برگردان
    else:
        return None  # در غیر این صورت، برنده‌ای وجود ندارد


#######################################################################
#                                                                     #
#                           START GAME                                #
#                                                                     #
#######################################################################
"""
این بخش از برنامه، براساس نوع بازی 
(`game_type`)
 اقدام به اجرای بازی می‌کند.

در صورتی که 
`game_type`
 برابر با 
 'Quick Match'
   باشد، یک بازی سریع 
   (`Quick Match`)
     ایجاد می‌شود. این بازی مبتنی بر بازی 
     Connect Four
       است و دو بازیکن اولیه به عنوان ورودی دریافت می‌شوند. سپس بازی آغاز می‌شود
         و نتیجه آن دریافت می‌شود. سپس نتیجه به عنوان ورودی برای یک شیء 
       ResultGUI
         استفاده می‌شود و با اجرای تابع 
         `start()`
         ، نتیجه به صورت گرافیکی نمایش داده می‌شود.

در صورتی که 
`game_type`
 برابر با 
 "League"
   باشد، تابع 
   `run_tournament`
     بازی تورنمنت را بین بازیکنان اجرا می‌کند. این تابع لیست بازیکنان
       را به عنوان ورودی دریافت می‌کند و مسابقات تورنمنت را بین آن‌ها برگزار می‌کند.
       در نهایت، برنده نهایی تورنمنت به عنوان خروجی
         برگردانده می‌شود. سپس نتیجه به عنوان ورودی برای یک شیء 
     ResultGUI
       استفاده می‌شود و با اجرای تابع 
       `start()`
       ، نتیجه به صورت گرافیکی نمایش داده می‌شود.
"""

if game_type == 'Quick Match':
    Quick_Match = ConnectFourGame(player_names[0], player_names[1])
    Quick_Match.start_game()
    result = Quick_Match.get_result()
    t = ResultGUI(result)
    t.start()
elif game_type == "League":

    winner = run_tournament(player_names)
    t = ResultGUI(winner)
    t.start()


