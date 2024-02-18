import speedtest
#by Wiktor Nosarzewski 18.02.2024 v2
def run_speed_test():
    print(f"Start! Speedtest by Wiktor Nosarzewski v2.0 18o2o24")
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  #Mbps
        upload_speed = st.upload() / 1_000_000  #Mbps

        download_speed2 = st.download() / 8_000_000  # Konwersja na MB/s
        upload_speed2 = st.upload() / 8_000_000  # Konwersja na MB/s

        print(f"Prędkość pobierania: {download_speed:.2f} Mbps")
        print(f"Prędkość wysyłania: {upload_speed:.2f} Mbps")
        print(f"Prędkość pobierania: {download_speed2:.2f} MB/s")
        print(f"Prędkość wysyłania: {upload_speed2:.2f} MB/s")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    run_speed_test()
