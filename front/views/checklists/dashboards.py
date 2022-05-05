from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from front.models import PageContents
import json


class ChecklistsDashboardsView(View):
    template_name = 'checklists/dashboards.html'

    def get(self, request):
        page_name = 'dashboards'
        try:
            page_content = PageContents.objects.filter(page_name=page_name)
            if page_content:
                page_content = page_content[0]
                statusInit = json.loads(page_content.status)
                ownerInit = json.loads(page_content.owners)
            else:
                ownerInit = [5, 10, 5, 1, 1, 5, 1, 5, 1]
                statusInit = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            id = [
                '1', '1', '1.1', '1.2', '1.3', '1', '1', '1.1', '1.2'
            ]
            description = [
                "Requirements", "PBI Access", "&nbsp;Access request", "&nbsp;Access rights", "&nbsp;App Link", "Requirements", "Online Dashboard URL", "&nbsp;Access request", "&nbsp;User creation"
            ]
            bold = [1, 1, 0, 0, 0, 1, 1, 0, 0]
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
                '<td align="left" class="pt-3-half" contenteditable="false">Power BI account to access the reports</td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Send an email to support.ar@maxerience.com, informing the client(s) which you want access to and email that will be used for login</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Assign the needed rights to the user(s) as per request</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Maxerience will share the link / instructions on how to access the transaction dashboard</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Maxerience Admin Portal user (same user is used for the online dashboard) </td>',
                '<td align="left" class="pt-3-half" contenteditable="false">http://statusdashboard.instagng.com/#</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Send an email to support.ar@maxerience.com, informing the client(s) which you want access to and email that will be used for login</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Maxerience support will team will create the user and assing the needed privileges</td>'
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
