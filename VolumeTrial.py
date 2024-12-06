# To test or purchase the source code, contact @SolVolSupp_bot on Telegram
# To test or purchase the source code, contact @SolVolSupp_bot on Telegram
# To test or purchase the source code, contact @SolVolSupp_bot on Telegram

import curses

def main_menu(stdscr):
    curses.curs_set(0)  # Hide the cursor

    menu = {
        "main": [
            ("🔊 Volume Bot", "volume"),
            ("💣 Army Snipe Bot", "army"),
            ("🤖 Bump Bot", "bump"),
            ("🔧 Create Token Bundler", "token"),
            ("💼 Wallet Set", "wallet"),
            ("📊 Liquidity Management", "liquidity_management"),
            ("🔄 Market-Making & Trading Bots", "market_making"),
            ("📦 Batch Operations", "batch_operations"),
            ("⚙️ Settings", "settings"),
            ("💰 Pump Strategies", "pump_strategies"),
            ("📜 Convenient Tools", "convenient_tools"),
            ("❌ Exit", "exit")
        ]
    }

    title = [
r" /      \ /      \|  \     |  \   |  \/      \|  \     |  \  |  \  \     /  \        \ ",
r"|  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓     | ▓▓   | ▓▓  ▓▓▓▓▓▓\ ▓▓     | ▓▓  | ▓▓ ▓▓\   /  ▓▓ ▓▓▓▓▓▓▓▓ ",
r"| ▓▓___\▓▓ ▓▓  | ▓▓ ▓▓     | ▓▓   | ▓▓ ▓▓  | ▓▓ ▓▓     | ▓▓  | ▓▓ ▓▓▓\ /  ▓▓▓ ▓▓__     ",
r" \▓▓    \| ▓▓  | ▓▓ ▓▓      \▓▓\ /  ▓▓ ▓▓  | ▓▓ ▓▓     | ▓▓  | ▓▓ ▓▓▓▓\  ▓▓▓▓ ▓▓  \    ",
r" _\▓▓▓▓▓▓\ ▓▓  | ▓▓ ▓▓       \▓▓\  ▓▓| ▓▓  | ▓▓ ▓▓     | ▓▓  | ▓▓ ▓▓\▓▓ ▓▓ ▓▓ ▓▓▓▓▓    ",
r"|  \__| ▓▓ ▓▓__/ ▓▓ ▓▓_____   \▓▓ ▓▓ | ▓▓__/ ▓▓ ▓▓_____| ▓▓__/ ▓▓ ▓▓ \▓▓▓| ▓▓ ▓▓_____ ",
r" \▓▓    ▓▓\▓▓    ▓▓ ▓▓     \   \▓▓▓   \▓▓    ▓▓ ▓▓     \\ ▓▓    ▓▓ ▓▓  \▓ | ▓▓ ▓▓     \ ",
r"  \▓▓▓▓▓▓  \▓▓▓▓▓▓ \▓▓▓▓▓▓▓▓    \▓     \▓▓▓▓▓▓ \▓▓▓▓▓▓▓▓ \▓▓▓▓▓▓ \▓▓      \▓▓\▓▓▓▓▓▓▓▓ "
     ]

    def print_menu(stdscr, selected_row_idx):
        stdscr.clear()
        # Print the title
        for i, line in enumerate(title):
            stdscr.addstr(i, 0, line, curses.color_pair(4))
        stdscr.addstr(len(title) + 1, 0, "Original Dev: @SolVolSupp_bot on Telegram", curses.color_pair(3))
        stdscr.addstr(len(title) + 2, 0, "Main Menu", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(len(title) + 3, 0, "Use arrow-keys. Return to submit.", curses.color_pair(3))

        # Print the menu
        current_menu_items = menu[current_menu]
        for idx, item in enumerate(current_menu_items):
            x = 0
            y = idx + len(title) + 5
            if idx == selected_row_idx:
                stdscr.addstr(y, x, item[0], curses.color_pair(1))
            else:
                stdscr.addstr(y, x, item[0])
        stdscr.refresh()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Highlighted menu item
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # Title color
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Subtitle color
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Bright green title color

    print_menu(stdscr)

    # Wait for user to exit
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main_menu)

# To test or purchase the source code, contact @SolVolSupp_bot on Telegram
