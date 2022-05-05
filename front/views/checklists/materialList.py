from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from front.models import PageContents
import json


class ChecklistsMaterialListView(View):
    template_name = 'checklists/material-list.html'

    def get(self, request):
        page_name = 'materialList'
        try:
            page_content = PageContents.objects.filter(page_name=page_name)
            if page_content:
                page_content = page_content[0]
                statusInit = json.loads(page_content.status)
                ownerInit = json.loads(page_content.owners)
            else:
                ownerInit = [1, 1, 7, 1, 1, 7, 7, 1, 1, 7, 7, 7, 7, 7, 1, 1, 1, 7, 7, 7, 7]
                statusInit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            id = [
                '2', '2.1', '2.2', '2.3',
                '3', '3.1', '3.2',
                '4', '4.1',
                '5', '5.1',
                '6',
                '7', '7.1',
                '8', '8.1', '8.2',
                '9', '9.1',
                '10', '10.1'
            ]
            description = [
                "GPU", "&nbsp;GPU to Power Supply cable", "&nbsp;#8 x 1/4 in Self-Drilling Screw ", "&nbsp;Antenna",
                "GPU Power Supply", "&nbsp;Power Cord for the Power Supply", "&nbsp;#8 x 1/4 in Self-Drilling Screw ",
                "Camera", "&nbsp;USB Data cable (Type A to Micro USB)",
                "Door Sensor *", "&nbsp;Door Sensor Cable*",
                "Magnet *",
                "Lock *", "&nbsp;Lock Cable *",
                "Payment Terminal **", "&nbsp;RJ45 to USB Cable (optional) **", "&nbsp;DB9 Female Head Connector",
                "Cooler Controller", "&nbsp;Controller to GPU cable",
                "Back Cover", "&nbsp;#8 x 1/4 in Self-Drilling Screw"
            ]
            bold = [1, 0, 0, 0, 1, 0, 0, 1, 0, 1,
                    0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0]
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
            quantity = [
                1, 1, 4, 2, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4
            ]
            part = [
                '', '001MAXCNV0002', '005MAXCNV0001', '', '003MAXCNV0001', '002MAXCNV0001', '006MAXCNV0001', '',
                '007MAXCNV0002', '009MAXCNV0001', '022MAXINV0001', '022MAXINV0001', '023MAXINV0001',
                '015MAXINV0001', '019MAXINV0001', '033MAXUSV0001', '034MAXUSV0001', '', '', '', '028MAXPLV0001'
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
                    "quantity": quantity[i],
                    "part": part[i],
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
