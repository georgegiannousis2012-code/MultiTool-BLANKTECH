#!/usr/bin/env python3
"""
BlankTech V3 - RedBox Edition (Safe Simulation)
ASCII-box themed terminal demo for Termux / any POSIX terminal.

IMPORTANT: This is a purely decorative demo. All features are simulated
and perform NO network access, NO attacks, NO data theft, and NO harmful actions.
Run with: python3 blanktech_redbox.py
"""

import os
import sys
import time
import random
import string
from datetime import datetime

# -----------------------
# ANSI Colors (Termux-friendly)
# -----------------------
class C:
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"

def color(text, col):
    return f"{col}{text}{C.RESET}"

# -----------------------
# Utilities
# -----------------------
def cls():
    os.system("clear")

def nowts():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# *** Changed to 0.5s as requested: every pause_short() call uses 0.5s ***
def pause_short():
    time.sleep(0.05)

def wait_enter(prompt="Press Enter to continue..."):
    try:
        input(color(prompt, C.YELLOW))
    except EOFError:
        pass

# -----------------------
# Banner ASCII (BlankTech in big letters)
# -----------------------
BANNER = r"""
██████╗ ██╗      █████╗ ███╗   ██╗██╗  ██╗████████╗███████╗ ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗████╗  ██║██║ ██╔╝╚══██╔══╝██╔════╝██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██╔██╗ ██║█████╔╝    ██║   █████╗  ██║     █████╔╝ 
██╔══██╗██║     ██╔══██║██║╚██╗██║██╔═██╗    ██║   ██╔══╝  ██║     ██╔═██╗ 
██████╔╝███████╗██║  ██║██║ ╚████║██║  ██╗   ██║   ███████╗╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝
"""

DEF_NOTICE = "(DEMO / EDUCATIONAL: Dont use the operations to harm anyone!)"

# -----------------------
# Box Drawing Helpers (ASCII lines)
# -----------------------
BOX_LEFT = "│"
BOX_RIGHT = "│"
BOX_TOP_LEFT = "┌"
BOX_TOP_RIGHT = "┐"
BOX_BOTTOM_LEFT = "└"
BOX_BOTTOM_RIGHT = "┘"
BOX_H = "─"
BOX_V = "│"
BOX_T_LEFT = "├"
BOX_T_RIGHT = "┤"
BOX_T_DOWN = "┬"
BOX_T_UP = "┴"
BOX_CROSS = "┼"

MENU_WIDTH = 64  # total inside width of the box
COLUMN_WIDTH = 30  # width of each column area

def box_top(title=None):
    line = BOX_TOP_LEFT + BOX_H * MENU_WIDTH + BOX_TOP_RIGHT
    print(color(line, C.RED))
    if title:
        title_line = BOX_V + title.center(MENU_WIDTH) + BOX_V
        print(color(title_line, C.RED))
        divider = BOX_T_LEFT + BOX_H * MENU_WIDTH + BOX_T_RIGHT
        print(color(divider, C.RED))
    else:
        spacer = BOX_V + " " * MENU_WIDTH + BOX_V
        print(color(spacer, C.RED))

def box_bottom():
    line = BOX_BOTTOM_LEFT + BOX_H * MENU_WIDTH + BOX_BOTTOM_RIGHT
    print(color(line, C.RED))

def box_blank_line():
    print(color(BOX_V + " " * MENU_WIDTH + BOX_V, C.RED))

def box_row(left_text, right_text=""):
    left = left_text.ljust(COLUMN_WIDTH)[:COLUMN_WIDTH]
    right = right_text.ljust(COLUMN_WIDTH)[:COLUMN_WIDTH]
    mid = "  "
    # compute trailing padding to match MENU_WIDTH
    trailing = MENU_WIDTH - 1 - COLUMN_WIDTH*2 - len(mid)
    if trailing < 0:
        trailing = 0
    row = BOX_V + " " + left + mid + right + " " * trailing + BOX_V
    print(color(row, C.RED))

def box_separator():
    sep = BOX_T_LEFT + BOX_H * MENU_WIDTH + BOX_T_RIGHT
    print(color(sep, C.RED))

# -----------------------
# Fake Data Generators (Harmless)
# -----------------------
def fake_name_email():
    vowels = "aeiou"
    consonants = "".join(set(string.ascii_lowercase) - set(vowels))
    parts = []
    for _ in range(random.choice([1,2])):
        syll = ''.join(random.choice(consonants) + random.choice(vowels) for _ in range(random.choice([1,1,2])))
        parts.append(syll)
    name = ''.join(parts)
    if random.random() < 0.6:
        name += str(random.randint(1,999))
    return name.lower()

def random_code(length):
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(length))

def fake_ip():
    return ".".join(str(random.randint(1,254)) for _ in range(4))

def fake_token():
    alphabet = string.ascii_letters + string.digits + "-_"
    parts = [
        ''.join(random.choice(alphabet) for _ in range(24)),
        ''.join(random.choice(alphabet) for _ in range(6)),
        ''.join(random.choice(alphabet) for _ in range(27))
    ]
    return ".".join(parts)

def fake_username():
    syllables = ["fer","do","ra","ki","to","mi","za","lo","ven","mar","ra","xi","neo"]
    name = ''.join(random.choice(syllables) for _ in range(random.randint(1,3)))
    if random.random() < 0.6:
        name += str(random.randint(1,999))
    return name

def random_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    return ''.join(random.choice(chars) for _ in range(length))

def fake_phone_number():
    country = random.choice(["+1", "+44", "+49", "+61", "+91", "+7"])
    return f"{country}{random.randint(100_000_000,999_999_999)}"

def random_bank_account():
    return ''.join(str(random.randint(0,9)) for _ in range(12))

def random_pin(length=4):
    return ''.join(str(random.randint(0,9)) for _ in range(length))

# -----------------------
# Demo Feature Implementations (SAFE, decorative)
# Keep same function names / behavior as prior demo, only cosmetic.
# -----------------------

def fake_ddos_panel():
    # Option 1 - kept behavior but safe and inside boxed UI
    while True:
        cls()
        draw_main_header()
        box_top("DDoS Attack")
        box_blank_line()
        box_row("Enter target identifier", "")
        box_blank_line()
        box_bottom()
        s = input(color("\nTarget > ", C.WHITE)).strip()
        if s.lower() == 'b':
            return
        if not s:
            print(color("No target entered. Press B to go back or enter a target.", C.YELLOW))
            time.sleep(0.8)
            continue
        print()
        print(color(f"Preparing attack to {s}...", C.YELLOW))
        for i in range(200):
            print(color(f"[{i+1:03}] Attack Sent to {s}", C.GREEN))
            pause_short()
        print(color("\nDone. This was a completed DDoS attack.", C.MAGENTA))
        wait_enter()
        return

def fake_email_creator():
    while True:
        cls()
        draw_main_header()
        box_top("Email Creator")
        box_blank_line()
        box_row("Generates 20  emails.", "")
        box_blank_line()
        box_bottom()
        choice = input(color("\nGenerate? (Y/B) > ", C.WHITE)).strip().lower()
        if choice == 'b':
            return
        if choice != 'y':
            print(color("Please enter 'Y' to generate or 'B' to go back.", C.YELLOW))
            time.sleep(0.6)
            continue
        domains = ["gmail.com", "yahoo.com", "outlook.com", "example.com", "mail.com"]
        print()
        for i in range(20):
            email = f"{fake_name_email()}@{random.choice(domains)}"
            print(color(f"{i+1:02}. {email}", C.GREEN))
            pause_short()
        print(color("\n20  emails generated .", C.MAGENTA))
        wait_enter()
        return

def fake_port_scanner():
    while True:
        cls()
        draw_main_header()
        box_top(" Port Scanner")
        box_blank_line()
        box_row("Displays 20  IP addresses.", "")
        box_blank_line()
        box_bottom()
        choice = input(color("\nScan? (Y/B) > ", C.WHITE)).strip().lower()
        if choice == 'b':
            return
        if choice != 'y':
            print(color("Please enter 'Y' to scan or 'B' to go back.", C.YELLOW))
            time.sleep(0.6)
            continue
        print()
        for i in range(20):
            ip = fake_ip()
            open_ports = random.sample([21,22,23,25,53,80,110,143,443,3306,8080], k=random.randint(0,3))
            ports_str = ", ".join(str(p) for p in open_ports) if open_ports else "none"
            print(color(f"{i+1:02}. {ip} - Open Ports: {ports_str}", C.GREEN))
            pause_short()
        print(color("\nScan complete .", C.MAGENTA))
        wait_enter()
        return

def fake_nitro_generator():
    while True:
        cls()
        draw_main_header()
        box_top(" Nitro Code Generator")
        box_blank_line()
        box_row("Generates 50 16-character codes.", "")
        box_blank_line()
        box_bottom()
        choice = input(color("\nGenerate? (Y/B) > ", C.WHITE)).strip().lower()
        if choice == 'b':
            return
        if choice != 'y':
            print(color("Please enter 'Y' to generate or 'B' to go back.", C.YELLOW))
            time.sleep(0.6)
            continue
        codes = [random_code(16) for _ in range(50)]
        for i, code in enumerate(codes):
            if i < 49:
                print(color(f"Nitro Code Failed ({code})", C.RED))
            else:
                print(color(f"Nitro Code Success ({code})", C.GREEN))
            pause_short()
        print(color("\nDone: 49 failed + 1 success.", C.MAGENTA))
        wait_enter()
        return

def fake_token_stealer():
    while True:
        cls()
        draw_main_header()
        box_top("Discord Bot Token Stealer")
        box_blank_line()
        box_row("Type bot name to attack.", "")
        box_blank_line()
        box_bottom()
        bot = input(color("\nBot name > ", C.WHITE)).strip()
        if bot.lower() == 'b':
            return
        if not bot:
            print(color("Enter a bot name or B to go back.", C.YELLOW))
            time.sleep(0.6)
            continue
        print(color(f"\nStarting  token attack against '{bot}' (simulation)...\n", C.YELLOW))
        for i in range(100):
            token = fake_token()
            if i < 99:
                print(color(f"[{i+1:03}] Token Attack Failed ({token})", C.RED))
            else:
                print(color(f"[{i+1:03}] Token Attack Successful ({token})", C.GREEN))
            pause_short()
        print(color("\nNote: All tokens above should be used legally.", C.MAGENTA))
        wait_enter()
        return

def fake_website_ddos():
    while True:
        cls()
        draw_main_header()
        box_top("Website DDoS")
        box_blank_line()
        box_row("Paste the URL (http/https).", "")
        box_blank_line()
        box_bottom()
        url = input(color("\nURL > ", C.WHITE)).strip()
        if url.lower() == 'b':
            return
        if not url:
            print(color("No URL entered. Press B to go back or enter a URL.", C.YELLOW))
            time.sleep(0.6)
            continue
        if not (url.startswith("http://") or url.startswith("https://")):
            print(color("Please include http:// or https:// at the start of the URL.", C.YELLOW))
            time.sleep(0.8)
            continue
        print(color(f"\nSimulating sending 200  attacks to {url}...\n", C.YELLOW))
        for i in range(200):
            print(color(f"[{i+1:03}] Sending Attack To {url}", C.GREEN))
            pause_short()
        print(color("\nDone. This was an online DDoS website attack.", C.MAGENTA))
        wait_enter()
        return

def fake_email_cracker():
    while True:
        cls()
        draw_main_header()
        box_top("Email Cracker")
        box_blank_line()
        box_row("Type the target email and press Enter", "")
        box_blank_line()
        box_bottom()
        email = input(color("\nEmail > ", C.WHITE)).strip()
        if email.lower() == 'b':
            return
        if not email or "@" not in email:
            print(color("Please enter a valid-looking email address or B to go back.", C.YELLOW))
            time.sleep(0.6)
            continue
        print(color(f"\nSimulating stealing database of {email}...\n", C.YELLOW))
        for i in range(100):
            print(color(f"[{i+1:03}] Stealing DataBase Of {email}", C.GREEN))
            pause_short()
        fake_phone = fake_phone_number()
        fake_pass = random_password(10)
        print(color("\nFound Results:", C.MAGENTA))
        print(color(f"Recovered phone: {fake_phone}", C.GREEN))
        print(color(f"Recovered password: {fake_pass}", C.GREEN))
        wait_enter()
        return

def fake_ip_lookup():
    while True:
        cls()
        draw_main_header()
        box_top("IP Lookup ")
        box_blank_line()
        box_row("Type an IP address (120.34.43).", "")
        box_blank_line()
        box_bottom()
        ip = input(color("\nIP > ", C.WHITE)).strip()
        if ip.lower() == 'b':
            return
        if not ip or len(ip.split(".")) != 4:
            print(color("Please enter a valid-looking IPv4 address or B to go back.", C.YELLOW))
            time.sleep(0.6)
            continue
        print(color(f"\nPrepairing lookup for {ip} and generating  account data...\n", C.YELLOW))
        platforms = [
            "Email", "Facebook", "Twitter", "Instagram", "PayPal", "BankAccount",
            "Xbox", "Steam", "Netflix", "Amazon", "GitHub", "LinkedIn", "Reddit"
        ]
        for plat in platforms:
            user = fake_username()
            pwd = random_password(random.randint(8,14))
            print(color(f"{plat} -> Username: {user} | Password: {pwd}", C.GREEN))
            pause_short()
        print(color(f"Phone -> {fake_phone_number()}", C.GREEN))
        pause_short()
        print(color(f"PayPal Password -> {random_password(12)}", C.GREEN))
        pause_short()
        print(color(f"Bank Account -> Acc:{random_bank_account()} | PIN:{random_pin(4)}", C.GREEN))
        pause_short()
        for i in range(10):
            plat = f"OtherPlatform{i+1}"
            print(color(f"{plat} -> Username: {fake_username()} | Password: {random_password(9)}", C.GREEN))
            pause_short()
        print(color("\nNote: All data above should not be used to harm anyone.", C.MAGENTA))
        wait_enter()
        return

def fake_wifi_cracker():
    while True:
        cls()
        draw_main_header()
        box_top("Wi-Fi Password Cracker")
        box_blank_line()
        box_row("Enter Wi-Fi SSID", "")
        box_blank_line()
        box_bottom()
        ssid = input(color("\nWi-Fi SSID > ", C.WHITE)).strip()
        if ssid.lower() == 'b':
            return
        if not ssid:
            print(color("Please enter an SSID or B to go back.", C.YELLOW))
            time.sleep(0.6)
            continue
        print(color(f"\nStarting  cracking for '{ssid}'...\n", C.YELLOW))
        for i in range(100):
            print(color(f"[{i+1:03}] Cracking Wifi Database", C.GREEN))
            pause_short()
        fake_user = fake_username()
        fake_pw = random_password(12)
        print(color(f"\nCrack complete . SSID: {ssid}", C.MAGENTA))
        print(color(f"Found network owner: {fake_user}", C.GREEN))
        pause_short()
        print(color(f"Found network password: {fake_pw}", C.GREEN))
        wait_enter()
        return

def fake_bypasser():
    while True:
        cls()
        draw_main_header()
        box_top("Fake Bypasser")
        box_blank_line()
        box_row("Enter the URL you want to bypass.", "")
        box_blank_line()
        box_bottom()
        url = input(color("\nURL > ", C.WHITE)).strip()
        if url.lower() == 'b':
            return
        if not url or not (url.startswith("http://") or url.startswith("https://")):
            print(color("Please enter a URL starting with http:// or https://, or B to go back.", C.YELLOW))
            time.sleep(0.6)
            continue
        print(color(f"\nSimulating BotNet Byppassing URL {url} 100 times ...\n", C.YELLOW))
        for i in range(100):
            print(color(f"[{i+1:03}] BotNet Byppassing URL {url}", C.GREEN))
            pause_short()
        print(color("\nDone. This was a BotNet bypass use them correctly and legaly.", C.MAGENTA))
        wait_enter()
        return

# ------------------ 11-20 SAFE SIMULATION FUNCTIONS ------------------

def sim_virus_builder():
    while True:
        cls()
        draw_main_header()
        box_top("Virus Builder - SIMULATION ONLY")
        box_blank_line()
        box_row("Stealer Options:", "")
        box_row(" 1. Discord Token Stealer (FAKE)", "")
        box_row(" 2. Browser Stealer (FAKE)", "")
        box_row(" 3. Discord Injection (FAKE)", "")
        box_row(" 4. Roblox Cookie Stealer (FAKE)", "")
        box_blank_line()
        box_row("Malware Options:", "")
        box_row(" 5. Keyboard Blocker (FAKE)", "")
        box_row(" 6. Mouse Blocker (FAKE)", "")
        box_row(" 7. Task Manager Blocker (FAKE)", "")
        box_row(" 8. Shutdown Trigger (FAKE)", "")
        box_row(" 9. Spam Window Opener (FAKE)", "")
        box_blank_line()
        box_row("Press 1-9 to build a fake payload, or B to go back.", "")
        box_blank_line()
        box_bottom()

        choice = input(color("\nSelect option (1-9) or B > ", C.WHITE)).strip().lower()
        if choice == 'b':
            return
        if choice not in [str(i) for i in range(1, 10)]:
            print(color("Invalid option — choose 1-9 or B.", C.YELLOW))
            time.sleep(0.6)
            continue

        module_name = module_name_from_choice(choice)
        print(color(f"\nBuilding simulated payload: {module_name}\n", C.MAGENTA))
        pause_short()

        steps = [
            "Initializing build environment...",
            "Loading dependencies...",
            "Compiling resources...",
            "Injecting simulation modules...",
            "Encrypting mock binary...",
            "Finalizing payload structure...",
            "Performing integrity check...",
            "Saving fake executable..."
        ]
        for i, step in enumerate(steps, start=1):
            print(color(f"[{i:02}] {step}", C.GREEN))
            pause_short()

        fake_file = f"payload_{random.randint(1000,9999)}.exe"
        print(color(f"\nFake build complete: {fake_file}", C.GREEN))
        pause_short()
        print(color("Reminder: This is a harmless visual demo only.", C.MAGENTA))
        wait_enter()
        return


def module_name_from_choice(choice):
    mapping = {
        '1': "DiscordTokenStealer-MOCK",
        '2': "BrowserCredentialGrabber-MOCK",
        '3': "DiscordInjectionStub-MOCK",
        '4': "RobloxCookieGrabber-MOCK",
        '5': "KeyboardBlocker-MOCK",
        '6': "MouseBlocker-MOCK",
        '7': "TaskMgrBlocker-MOCK",
        '8': "ShutdownTrigger-MOCK",
        '9': "SpamWindow-MOCK"
    }
    return mapping.get(choice, "Unknown-Module")
 
def sim_tiktok_follow_bot():
    while True:
        cls()
        draw_main_header()
        box_top("TikTok Follow Bot - ")
        box_blank_line()
        box_row("Enter username and unlock code (x100blank to unlock 1000)", "")
        box_blank_line()
        box_bottom()
        user = input(color("\nUsername > ", C.WHITE)).strip()
        if user.lower() == 'b' or user == '':
            return
        code = input(color("VIP unlock code (press Enter to skip) > ", C.WHITE)).strip()
        max_followers = 1000 if code.lower() == "x100blank" else 200
        print(color(f"Max followers allowed: {max_followers}", C.YELLOW))
        try:
            amount = int(input(color(f"Amount to send (1-{max_followers}) > ", C.WHITE)).strip())
        except Exception:
            print(color("Invalid number.", C.RED))
            time.sleep(0.6)
            continue
        if amount < 1 or amount > max_followers:
            print(color("Amount out of allowed range.", C.RED))
            time.sleep(0.6)
            continue
        print(color(f"\nSimulating sending {amount} bot followers to @{user}...\n", C.YELLOW))
        for i in range(amount):
            print(color(f"[{i+1:03}] Bot Follower sent to @{user}", C.GREEN))
            pause_short()
        print(color("\nOperation complete.", C.MAGENTA))
        wait_enter()
        return

def sim_mass_report():
    while True:
        cls()
        draw_main_header()
        box_top("Mass Report - ")
        box_blank_line()
        box_row("Enter platform and username. Unlock code x100blank for extended range", "")
        box_blank_line()
        box_bottom()
        platform = input(color("\nPlatform > ", C.WHITE)).strip()
        if platform.lower() == 'b' or platform == '':
            return
        username = input(color("Username (without @) > ", C.WHITE)).strip().lstrip("@")
        code = input(color("VIP unlock code (press Enter to skip) > ", C.WHITE)).strip()
        max_reports = 1000 if code.lower() == "x100blank" else 200
        print(color(f"Max reports allowed: {max_reports}", C.YELLOW))
        try:
            amount = int(input(color(f"Amount to send (1-{max_reports}) > ", C.WHITE)).strip())
        except Exception:
            print(color("Invalid number.", C.RED))
            time.sleep(0.6)
            continue
        if amount < 1 or amount > max_reports:
            print(color("Amount out of allowed range.", C.RED))
            time.sleep(0.6)
            continue
        print(color(f"\nSimulating reporting @{username} on {platform} {amount} times...\n", C.YELLOW))
        for i in range(amount):
            print(color(f"[{i+1:03}] Reported @{username} from {platform}", C.GREEN))
            pause_short()
        print(color("\nOperation complete .", C.MAGENTA))
        wait_enter()
        return

def sim_email_bomber():
    while True:
        cls()
        draw_main_header()
        box_top("Email Bomber - ")
        box_blank_line()
        box_row("Enter target email to bomb", "")
        box_blank_line()
        box_bottom()
        email = input(color("\nEmail > ", C.WHITE)).strip()
        if email.lower() == 'b' or email == '':
            return
        amount = 200
        print(color(f"\nBotNet attack sending {amount} mails to {email}...\n", C.YELLOW))
        for i in range(amount):
            print(color(f"[{i+1:03}] Bomb attacking {email}", C.GREEN))
            pause_short()
        print(color("\nOperation complete .", C.MAGENTA))
        wait_enter()
        return

def sim_vpn_connect():
    while True:
        cls()
        draw_main_header()
        box_top("VPN Connect - ")
        box_blank_line()
        box_row("Enter country and optional site ", "")
        box_blank_line()
        box_bottom()
        country = input(color("\nCountry > ", C.WHITE)).strip()
        if country.lower() == 'b' or country == '':
            return
        site = input(color("Site to access (optional) > ", C.WHITE)).strip()
        print(color(f"\nSimulating connection to VPN server for {country}...\n", C.YELLOW))
        for i in range(100):
            print(color(f"[{i+1:03}] Connecting VPN server ({country})", C.GREEN))
            pause_short()
        fake_ipaddr = fake_ip()
        print(color(f"\nConnected to {country} via {fake_ipaddr} (SIMULATION).", C.MAGENTA))
        if site:
            print(color(f"Target site path: {site} .", C.MAGENTA))
        wait_enter()
        return

def sim_vpn_bypasser():
    while True:
        cls()
        draw_main_header()
        box_top("VPN Bypasser - ")
        box_blank_line()
        box_row("Enter VPN IP to pass", "")
        box_blank_line()
        box_bottom()
        vpn_ip = input(color("\nVPN IP > ", C.WHITE)).strip()
        if vpn_ip.lower() == 'b' or vpn_ip == '':
            return
        print(color(f"\nPreparing breaking VPN system for {vpn_ip}...\n", C.YELLOW))
        for i in range(100):
            print(color(f"[{i+1:03}] Breaking VPN system", C.GREEN))
            pause_short()
        generated = fake_ip()
        print(color(f"\nOperation result: Generated fallback IP: {generated}", C.MAGENTA))
        wait_enter()
        return

def sim_ipv4_bypasser():
    while True:
        cls()
        draw_main_header()
        box_top("IPv4 Bypasser -")
        box_blank_line()
        box_row("Enter IPv4 to gateway", "")
        box_blank_line()
        box_bottom()
        ip = input(color("\nIPv4 > ", C.WHITE)).strip()
        if ip.lower() == 'b' or ip == '':
            return
        print(color(f"\nPreparing IPv4 bypass for {ip}...\n", C.YELLOW))
        for i in range(100):
            print(color(f"[{i+1:03}] Breaking IPv4 gateway", C.GREEN))
            pause_short()
        generated = fake_ip()
        print(color(f"\nOperation completed  IP: {generated}", C.MAGENTA))
        wait_enter()
        return

def sim_message_reactor():
    while True:
        cls()
        draw_main_header()
        box_top("Message Reactor - ")
        box_blank_line()
        box_row("Enter message ID and emoji short-code", "")
        box_blank_line()
        box_bottom()
        msgid = input(color("\nMessage ID > ", C.WHITE)).strip()
        if msgid.lower() == 'b' or msgid == '':
            return
        emoji = input(color("Emoji short-code (e.g. :skull:) > ", C.WHITE)).strip()
        print(color(f"\nBots sending reactions {emoji} to message {msgid}...\n", C.YELLOW))
        for i in range(100):
            print(color(f"[{i+1:03}] Sending Reacts to {msgid} -> {emoji}", C.GREEN))
            pause_short()
        print(color("\nOperation complete.", C.MAGENTA))
        wait_enter()
        return

def sim_botnet_maker():
    while True:
        cls()
        draw_main_header()
        box_top("BotNet Maker -")
        box_blank_line()
        box_row("Enter target and optional unlock code (x100blank) for more agents", "")
        box_blank_line()
        box_bottom()
        target = input(color("\nTarget > ", C.WHITE)).strip()
        if target.lower() == 'b' or target == '':
            return
        code = input(color("VIP unlock code (press Enter to skip) > ", C.WHITE)).strip()
        max_runs = 1000 if code.lower() == "x100blank" else 100
        try:
            amount = int(input(color(f"Amount to simulate (1-{max_runs}) > ", C.WHITE)).strip())
        except Exception:
            print(color("Invalid number.", C.RED))
            time.sleep(0.6)
            continue
        if amount < 1 or amount > max_runs:
            print(color("Amount out of allowed range.", C.RED))
            time.sleep(0.6)
            continue
        print(color(f"\nSimulating activation of {amount} botnet agents for {target}...\n", C.YELLOW))
        for i in range(amount):
            print(color(f"[{i+1:03}] BotNet is active (ID-{random.randint(10000,99999)})", C.GREEN))
            pause_short()
        print(color("\nOperation complete.", C.MAGENTA))
        wait_enter()
        return

def sim_phishing_mock_ui():
    platforms = [
        "Snapchat", "Instagram", "Facebook", "Twitter", "TikTok", "LinkedIn",
        "Gmail", "Yahoo Mail", "Outlook", "Netflix", "Spotify", "Amazon",
        "Steam", "Roblox", "Xbox Live", "PayPal", "GitHub", "Reddit",
        "Discord", "Pinterest"
    ]
    while True:
        cls()
        draw_main_header()
        box_top("Phishing Mock UI - ")
        box_blank_line()
        box_row("Select platform number to show a harmfull credential demo", "")
        box_blank_line()
        half = len(platforms)//2
        for i in range(half):
            left = f"{i+1}. {platforms[i]}"
            right = f"{i+1+half}. {platforms[i+half]}"
            box_row(left, right)
        box_blank_line()
        box_row("Enter number or B to go back", "")
        box_blank_line()
        box_bottom()
        sel = input(color("\nSelect a platform number > ", C.WHITE)).strip().lower()
        if sel == 'b':
            return
        if not sel.isdigit() or not (1 <= int(sel) <= len(platforms)):
            print(color("Invalid selection.", C.RED))
            time.sleep(0.6)
            continue
        idx = int(sel)-1
        platform = platforms[idx]
        username = input(color(f"Enter username for {platform}  > ", C.WHITE)).strip()
        if not username:
            print(color("No username entered.", C.YELLOW))
            time.sleep(0.6)
            continue
        print(color(f"\nPreparing credential lookup for {username} on {platform}...\n", C.YELLOW))
        for i in range(6):
            print(color(f"[{i+1:02}] Querying mock database...", C.GREEN))
            pause_short()
        print(color("\nFOUND RECOVERED DATA (placeholders):", C.MAGENTA))
        print(color(f"Username: {username}", C.GREEN))
        pause_short()
        print(color(f"Password: {random_password(10)}", C.GREEN))
        pause_short()
        print(color(f"Email linked: {fake_name_email()}@example.com", C.GREEN))
        pause_short()
        print(color(f"Phone: {fake_phone_number()}", C.GREEN))
        wait_enter()
        return

# -----------------------
# Draw main boxed menu (two-column 1-10 | 11-20)
# -----------------------
def draw_main_header():
    cls()
    print(color(BANNER, C.RED))
    print(color(DEF_NOTICE.center(MENU_WIDTH), C.YELLOW))
    print()
    box_top("BlankTech - RedBox Edition")
    box_blank_line()
    left = [f"[{i}] {label_for(i)}" for i in range(1,11)]
    right = [f"[{i}] {label_for(i)}" for i in range(11,21)]
    for i in range(10):
        l = left[i]
        r = right[i]
        box_row(l, r)
    box_blank_line()
    box_bottom()
    print()

def label_for(n):
    labels = {
        1: "DDoS Attack ",
        2: "Email Creator",
        3: "Port Scanner",
        4: "Nitro Code Generator",
        5: "Discord Bot Token Stealer",
        6: "Website DDoS ",
        7: "Email Cracker",
        8: "IP Lookup ",
        9: "Wi-Fi Password Cracker",
        10:"Bypasser ",
        11:"Virus Builder",
        12:"TikTok Follow Bot",
        13:"Mass Report ",
        14:"Email Bomber",
        15:"VPN Connect",
        16:"VPN Bypasser",
        17:"IPv4 Bypasser",
        18:"Message Reactor",
        19:"BotNet Maker",
        20:"Phishing Mock UI",
    }
    return labels.get(n, f"Feature {n}")

# -----------------------
# Feature map (string keys)
# -----------------------
FEATURE_MAP = {
    "1": fake_ddos_panel,
    "2": fake_email_creator,
    "3": fake_port_scanner,
    "4": fake_nitro_generator,
    "5": fake_token_stealer,
    "6": fake_website_ddos,
    "7": fake_email_cracker,
    "8": fake_ip_lookup,
    "9": fake_wifi_cracker,
    "10": fake_bypasser,
    "11": sim_virus_builder,
    "12": sim_tiktok_follow_bot,
    "13": sim_mass_report,
    "14": sim_email_bomber,
    "15": sim_vpn_connect,
    "16": sim_vpn_bypasser,
    "17": sim_ipv4_bypasser,
    "18": sim_message_reactor,
    "19": sim_botnet_maker,
    "20": sim_phishing_mock_ui,
}

# -----------------------
# Main loop
# -----------------------
def main():
    while True:
        draw_main_header()
        print(color("Select an option (1-20) or Q to quit:", C.WHITE))
        choice = input(color(">>> ", C.RED)).strip().lower()
        if choice == "q":
            print(color("\nExiting BlankTech RedBox Edition. Goodbye!", C.RED))
            time.sleep(0.5)
            break
        if choice in FEATURE_MAP:
            try:
                FEATURE_MAP[choice]()
            except Exception as e:
                print(color("An unexpected error occurred.", C.RED))
                print(color(str(e), C.RED))
                time.sleep(1.0)
        else:
            print(color("Invalid selection - choose 1-20 or Q.", C.RED))
            time.sleep(0.7)

# -----------------------
# Entrypoint
# -----------------------
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + color("Interrupted. Exiting BlankTech demo.", C.MAGENTA))
        sys.exit(0)