from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from front.models import PageContents
import json


class ChecklistsPaymentIntegrationView(View):
    template_name = 'checklists/payment-integration.html'

    def get(self, request):
        page_name = 'paymentIntegration'
        try:
            page_content = PageContents.objects.filter(page_name=page_name)
            if page_content:
                page_content = page_content[0]
                statusInit = json.loads(page_content.status)
                ownerInit = json.loads(page_content.owners)
            else:
                ownerInit = [10, 5, 6, 10, 6, 6, 10, 9, 9, 9, 3, 3, 3, 3, 9, 9]
                statusInit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            id = [
                '1', '1.1', '1.2',
                '2', '2.1', '2.2',
                '3', '3.1', '3.2', '3.3',
                '4', '4.1',
                '5', '5.1', '5.2', '5.2.1'
            ]
            description = [
                "Gateway", "&nbsp;Gateway definition", "&nbsp;Gateway documentation",
                "Flow", "&nbsp;Card Validation", "&nbsp;Pre-authorization",
                "Card management", "&nbsp;Store multiple cards", "&nbsp;Set default card", "&nbsp;Delete cards",
                "Incremental authorization", "&nbsp;Pending payments",
                "Integration", "&nbsp;APIs definition", "&nbsp;Bottler integration", "&nbsp;&nbsp;Fiscal integration (promos)"
            ]
            bold = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0]
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
                '<td align="left" class="pt-3-half" contenteditable="false">Cross check with Vending Team</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">https://developercielo.github.io/manual/cielo-ecommerce \
                    <button class="btn-card" onclick="window.open(\'/static/assets/download/psyment/Presentation in Maxerience Training Framework Material v0.3.pptx\')"> \
                        <div class="cardxls">  \
                            <img src="/static/assets/image/pptx.png"> \
                            <label>CC_Payme ntAPIv1.pptx</label> \
                        </div> \
                    </button> \
                </td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">https://developercielo.github.io/manual/cielo-ecommerce#zero-auth</td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">PPT item 1.2</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Internal development</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">PPT item 1.2</td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">PPT item 1.2</td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">PPT item 1.2</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">PPT item 1.2</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">PPT item 1.2</td>'
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
