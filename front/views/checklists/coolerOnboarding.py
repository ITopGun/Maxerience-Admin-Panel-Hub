from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from front.models import PageContents
import json


class ChecklistsCoolerOnboardingView(View):
    template_name = 'checklists/cooler-onboarding.html'

    def get(self, request):
        page_name = 'coolerOnboarding'
        try:
            page_content = PageContents.objects.filter(page_name=page_name)
            if page_content:
                page_content = page_content[0]
                statusInit = json.loads(page_content.status)
                ownerInit = json.loads(page_content.owners)
            else:
                ownerInit = [10, 1, 1, 10, 1, 10, 7, 5,
                            3, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 5]
                statusInit = [0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            id = [
                '1', '1.1', '1.2',
                '2', '2.1',
                '3', '3.1', '3.2',
                '4', '4.1',
                '5', '5.1', '5.2',
                '6', '6.1', '6.2',
                '7', '7.1', '7.2', '7.3'
            ]
            description = [
                "Smart device", "&nbsp;Smart device creation", "&nbsp;MAC Address association",
                "QR Code", "&nbsp;QR Code creation",
                "Asset", "&nbsp;Cooler SN", "&nbsp;Asset Creation",
                "Outlet", "&nbsp;Outlet creation (Outlet MD)",
                "Association", "&nbsp;Smart Device & Asset", "&nbsp;Outlet & Asset",
                "Planogram", "&nbsp;Planogram definition", "&nbsp;Planogram setup",
                "Pricing", "&nbsp;Standar Price Creation", "&nbsp;Promotion per cooler update",  "&nbsp;Planogram and prices - Outlet assossiation"
            ]
            bold = [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
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
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">GPU assignment</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">MAC Address and GPU association</td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">QR Code generation</td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">OEM SN</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">OEM SN and Maxerience asset association; This step could be done by Maxerience team, via support request</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">This step could be done by Maxerience team, via support request</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">This step could be done by Maxerience team, via support request</td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">This step could be done by Maxerience team, via support request</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">This step could be done by Maxerience team, via support request</td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Definition of the products that will be available in the coolers</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">This step could be done by Maxerience team, via support request</td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">This step could be done by Maxerience team, via support request</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">This step could be done by Maxerience team, via support request</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">This step could be done by Maxerience team, via support request</td>'
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
