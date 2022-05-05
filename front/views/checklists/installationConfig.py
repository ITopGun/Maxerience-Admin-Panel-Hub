from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from front.models import PageContents
import json


class ChecklistsInstallationConfigView(View):
    template_name = 'checklists/installation-config.html'

    def get(self, request):
        page_name = 'installationConfig'
        try:
            page_content = PageContents.objects.filter(page_name=page_name)
            if page_content:
                page_content = page_content[0]
                statusInit = json.loads(page_content.status)
                ownerInit = json.loads(page_content.owners)
            else:
                ownerInit = [10, 10, 1, 1, 1, 1, 10, 1, 1, 1, 10, 9, 9, 9, 9]
                statusInit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            id = [
                '4', '4.1', '4.1.1', '4.1.2', '4.1.3', '4.1.4',
                '4.2', '4.2.1', '4.2.2', '4.2.3',
                '4.3', '4.3.1', '4.3.2', '4.3.3', '4.3.4'
            ]
            description = [
                "Installation & Configuration", "&nbsp;Logical (Admin Portal)", "&nbsp;&nbsp;Smart device - Creation & Association", "&nbsp;&nbsp;Asset - creation & association", "&nbsp;&nbsp;", "&nbsp;&nbsp;Outlet - association", "&nbsp;&nbsp;QR Code",
                "&nbsp;SW (GPU)", "&nbsp;&nbsp;APN Configuration", "&nbsp;&nbsp;Base Apps", "&nbsp;&nbsp;Recognition system apps",
                "&nbsp;Physical", "&nbsp;&nbsp;Retrofit", "&nbsp;&nbsp;HW health check", "&nbsp;&nbsp;Dashboard verification", "&nbsp;&nbsp;Tracker (red line) adjusment"
            ]
            bold = [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0]
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
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">MAC Address association</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Association of the Smart Device & cooler SN</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Association of the asset & outlet</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Generation of the unique cooler QR Code</td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">APN configuration to enable the Sim Card attachement to the mobile network</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">DWS & hw/cloud management commucation applications</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Model, MisClient, MCU and Algorithm</td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Installation of the kit parts</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">GPU, cameras, door lock, door sensor and all components health status and SW versions if applicable</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Check cooler and components status in the Dashboard</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Fine tunning for betterrecognition and tracking of the products during transactions</td>'
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
