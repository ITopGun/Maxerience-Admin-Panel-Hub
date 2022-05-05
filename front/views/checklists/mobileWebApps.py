from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from front.models import PageContents
import json


class ChecklistsMobileWebAppsView(View):
    template_name = 'checklists/mobile-web-apps.html'

    def get(self, request):
        page_name = 'mobileWebApps'
        try:
            page_content = PageContents.objects.filter(page_name=page_name)
            if page_content:
                page_content = page_content[0]
                statusInit = json.loads(page_content.status)
                ownerInit = json.loads(page_content.owners)
            else:
                ownerInit = [10, 3, 3, 2, 2, 3, 2, 3, 10, 3, 3, 3, 3, 3, 10,
                            4, 4, 4, 4, 4, 4, 10, 3, 10, 10, 3, 7, 7, 7, 7, 7, 7, 7]
                statusInit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            id = [
                '1', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7',
                '2', '2.1', '2.2', '2.3', '2.4', '2.5',
                '3', '3.1', '3.2', '3.3', '3.4', '3.5', '3.6',
                '4', '4.1',
                '5', '5.1', '5.1.1', '5.2', '5.3', '5.4', '5.5', '5.6', '5.7', '5.8'
            ]
            description = [
                "General", "&nbsp;Mobile App", "&nbsp;Web App", "&nbsp;App Name", "&nbsp;App Icon", "&nbsp;Stores Description", "&nbsp;Stores preview images", "&nbsp;Landing Page",
                "Translation", "&nbsp;Screens", "&nbsp;Landing Page", "&nbsp;Account activation email", "&nbsp;Account activation landing page", "&nbsp;Forgot / Reset password",
                "Legal", "&nbsp;Age verification", "&nbsp;Terms of use & sale", "&nbsp;Privacy Policy", "&nbsp;Do not sell my information", "&nbsp;Menus", "&nbsp;FAQ",
                "Marketing & Promos", "&nbsp;Buy 10 Get 1 Free",
                "Flow", "&nbsp;Signup process", "&nbsp;&nbsp;Required fields", "&nbsp;Card Validation", "&nbsp;Pre-authorization", "&nbsp;Store multiple cards", "&nbsp;Set default card", "&nbsp;Delete card(s)", "&nbsp;Incremental authorization", "&nbsp;Pending payments"
            ]
            bold = [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0,
                    0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
            owners = [
                {"value": str("1"), "text": "Maxerience"},
                {"value": str("2"), "text": "Global"},
                {"value": str("3"), "text": "OU/D2C"},
                {"value": str("4"), "text": "OU/Legal"},
                {"value": str("5"), "text": "OU/Bottler"},
                {"value": str("6"), "text": "OU/Provider"},
                {"value": str("7"), "text": "OEM"},
                {"value": str("8"), "text": "All"},
                {"value": str("9"), "text": "OEM & Maxerience"},
                {"value": str("0"), "text": "Max & Provider"},
                {"value": str("10"), "text": ""}
            ]
            statuses = [
                {"value": str("0"), "text": "Not Started"},
                {"value": str("1"), "text": "In Progress"},
                {"value": str("2"), "text": "Delayed"},
                {"value": str("3"), "text": "Complete"},
            ]
            notes = [
                '<td align="left" class="pt-3-half" contenteditable="false">Not applicable in countries where the app is already integrated / released</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Mobile app usage or not</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Web app usage or not</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">CokeNow</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Temporary option while new Global Brand & VIS is being created \
                    <button class="btn-card" onclick="window.open(\'/static/assets/download/application/1.png\')"> \
                        <div class="cardapp">  \
                            <img class="cardappimg" src="/static/assets/image/appicon.png"> \
                        </div> \
                    </button> \
                    </td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Description of the app in the official stores</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Images of the app in the official stores (Can be adjusted if OU request)</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">If the end user scans the QR code without the app</td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">All screens from the apps (native & web)</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">https://cokenow-vending-machine.azurewebsites.net/ContinueOption</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">https://cooperholdingscorp.app.box.com/s/2eqem8nxnis79z7l96u5zc12966nqrsl</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">https://portal-prod.maxerience.com/CokeNowActivationSuccess.html</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Email to be sent to recover/change the app password</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Examples: Mobile Apps Checklist</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">ex: 13+ </td>',
                '<td align="left" class="pt-3-half" contenteditable="false">https://us.coca-cola.com/terms-of-use</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">https://us.coca-cola.com/privacy-policy#privacy</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">https://us.coca-cola.com/privacy-policy#rights</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Any specific condition needed in the app menus, for legal compliance \
                    <button class="btn-card" onclick="window.open(\'/static/assets/download/application/1.pptx\')"> \
                        <div class="cardxls">  \
                            <img src="/static/assets/image/pptx.png"> \
                            <label>USPCP Toolkit for Websites and Mobile Apps.pptx</label> \
                        </div> \
                    </button> \
                    </td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Frequently asked questions \
                    <button class="btn-card" onclick="window.open(\'/static/assets/download/application/33.doc\')"> \
                        <div class="cardxls">  \
                            <img src="/static/assets/image/docx.png"> \
                            <label>CokeNow App FAQ.docx</label> \
                        </div> \
                    </button> \
                    </td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">OPTIONAL Promotion that consists on rewarding users with one free product once 10 are purchased \
                    <button class="btn-card" onclick="window.open(\'/static/assets/download/application/w.docx\')"> \
                        <div class="cardxls">  \
                            <img src="/static/assets/image/docx.png"> \
                            <label>B10G1_GINAL Terms.docx</label> \
                        </div> \
                    </button> \
                    </td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Mandatory fields for signup process (some local regulations need additional fields)</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Is the card validated while adding it in the apps?</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Is a pre-authorization required for unlocking the cooler door?</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Is it needed to have the possibility of storing multiple cards?</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Is it needed to have the possibility of setting one default card?</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Is it need to have the possibility of deleting cards?</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">In case pre-authorization is used, what should happen in case the purchase exceeds the pre-authorization value?</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">If a payment is rejected, how this should be managed (try again, add another card, try again once the user tries a new purchase)?</td>'
            ]
            ownerColors = ["#C00000", "#FFC000", "red", "#FCE4D6", "#FFF2CC",
                           "#E2EFDA", "#548235", "#0070C0", "#FFFF00", "#7030A0", "#FFFFFF"]
            statusColors = ["grey", "#EAC282", "#D65532", "green"]

            result = []
            for i in range(len(id)):
                result.append({
                    "id": id[i],
                    "description": description[i],
                    "bold": bold[i],
                    "ownerInit": str(ownerInit[i]),
                    "statusInit": statusInit[i],
                    "notes": notes[i],
                    "index": i,
                    "ownerColor": ownerColors[int(ownerInit[i])],
                    "statusColor": statusColors[int(statusInit[i])]
                })
            if request.user.is_authenticated:
                return render(request, self.template_name, {"result": result, "statuses": statuses, "owners": owners})
            else:
                return redirect('/select-customer/')
        except Exception as e:
            return JsonResponse({'status': 400, 'message': str(e)})
