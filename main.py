import flet as ft
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def main(page: ft.Page):
    def getinfo(self):
        c1.controls.pop()
        try:
            parsed_number = phonenumbers.parse(txt.value, "IN")
            phone_number = txt.value
            is_valid_number = phonenumbers.is_valid_number(parsed_number)
            country_code = phonenumbers.region_code_for_number(parsed_number)
            country_name = geocoder.description_for_number(parsed_number, "en")
            region = geocoder.region_code_for_number(parsed_number)
            carrier_info = carrier.name_for_number(parsed_number, "en")
            timezone_info = timezone.time_zones_for_number(parsed_number)
            timezone_str = timezone_info[0] if timezone_info else "Unknown"
            international_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            national_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
            e164_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
            
            intxt = ft.Text(
                value=f"Phone Number Information\n"
                      f"Number : {phone_number}\n"
                      f"Is Valid Number : {is_valid_number}\n"
                      f"Country Code : {country_code}\n"
                      f"Country Name : {country_name}\n"
                      f"Region : {region}\n"
                      f"Carrier Info : {carrier_info}\n"
                      f"Timezone : {timezone_str}\n"
                      f"International Format : {international_format}\n"
                      f"National Format : {national_format}\n"
                      f"E.164 Format : {e164_format}",
                size=15,
                weight='bold',
                text_align='left',
                color=ft.colors.YELLOW_ACCENT,
            )
            cls = ft.ElevatedButton(
                text='Try Another',
                bgcolor=ft.colors.YELLOW_ACCENT,
                height=50,
                width=300,
                color=ft.colors.BLACK,
                on_click=clears 
            )
            c1.controls.append(intxt)
            c1.controls.append(cls)
        except phonenumbers.phonenumberutil.NumberParseException as e:
            intxt = ft.Text(
                value=f"Invalid phone number : {e}",
                size=15,
                weight='bold',
                text_align='left',
                color=ft.colors.RED,
            )
            cls = ft.ElevatedButton(
                text='Try Another',
                bgcolor=ft.colors.YELLOW_ACCENT,
                height=50,
                width=300,
                color=ft.colors.BLACK,
                on_click=clears 
            )
            c1.controls.append(intxt)
            c1.controls.append(cls)
        page.update()

    def clears(self):
        c1.controls.clear()
        c1.controls.append(txt)
        txt.value = ""
        page.update()

    r1 = ft.Row(
        controls=[
            ft.Text(
                value='VIMOWEB',
                size=60,
                weight='bold',
                text_align='center',
                color=ft.colors.YELLOW_ACCENT
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    txt = ft.TextField(
        hint_text='Type Something...',
        multiline=False,
        width=300,
        height=50,
        color=ft.colors.YELLOW_ACCENT,
        border_radius=ft.border_radius.all(10),
        border_color=ft.colors.YELLOW_ACCENT,
    )
    c1 = ft.Column(
        controls=[txt],
        height=400,
        width=300,
        alignment=ft.MainAxisAlignment.CENTER,
    )
    cons = ft.Container(
        content=c1,
        alignment=ft.alignment.center
    )
    r3 = ft.Row(
        controls=[
            ft.ElevatedButton(
                text='Get Information',
                bgcolor=ft.colors.GREEN_700,
                height=50,
                width=200,
                color=ft.colors.WHITE,
                on_click=getinfo
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    page.add(r1, cons, r3)

ft.app(main)
