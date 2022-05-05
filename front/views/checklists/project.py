from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from front.models import PageContents
import json


class ChecklistsProjectView(View):
    template_name = 'checklists/project.html'

    def get(self, request):
        page_name = 'project'
        try:
            page_content = PageContents.objects.filter(page_name=page_name)
            if page_content:
                page_content = page_content[0]
                statusInit = json.loads(page_content.status)
                ownerInit = json.loads(page_content.owners)
            else:
                ownerInit = [0, 10, 8, 8, 10, 1, 9, 10, 10, 5, 8, 8, 8, 8, 8, 8, 5, 1,
                             5, 5, 10, 1, 1, 9, 0, 1, 1, 9, 1, 1, 5, 5, 10, 1, 1, 10, 5, 10, 8]
                statusInit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            id = [
                '1', '1.1', '1.1.1', '1.1.2',
                '2', '2.1', '2.2',
                '3', '3.1', '3.1.1', '3.1.2', '3.1.3', '3.1.4', '3.1.5', '3.1.6',
                '3.2', '3.2.1', '3.2.2', '3.2.3', '3.2.4',
                '4', '4.1', '4.2', '4.3',
                '5', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6', '5.7',
                '6', '6.1', '6.2',
                '7', '7.1',
                '8', '8.1'
            ]
            description = [
                "Kick-off Meeting", "&nbsp;Initial agreements", "&nbsp;&nbsp;Main contacts", "&nbsp;&nbsp;Matrix of responsibilities",
                "Requirements & Material list", "&nbsp;Solution requirements document", "&nbsp;BOM (Material list)",
                "Project Scope", "&nbsp;Apps", "&nbsp;&nbsp;Payment Gateway", "&nbsp;&nbsp;General", "&nbsp;&nbsp;Translation", "&nbsp;&nbsp;Legal", "&nbsp;&nbsp;Marketing & Promos", "&nbsp;&nbsp;Flow",
                "&nbsp;Master Data & Package / Label Training", "&nbsp;&nbsp;SKUs", "&nbsp;&nbsp;Model ", "&nbsp;&nbsp;Product MD", "&nbsp;&nbsp;Outlet MD",
                "Installation & Configuration", "&nbsp;Logical (Admin Portal)", "&nbsp;SW (GPU)", "&nbsp;Physical",
                "Cooler Onboarding", "&nbsp;Smart Device", "&nbsp;QR Code", "&nbsp;Asset", "&nbsp;Outlet", "&nbsp;Association", "&nbsp;Planogram", "&nbsp;Pricing",
                "Training", "&nbsp;Installation, configuration & troubleshooting documentation", "&nbsp;Level 1 training - Camera cooler solution",
                            "Go Live", "&nbsp;Cooler placement on site",
                            "Project Closure", "&nbsp;Review meeting"
            ]
            bold = [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0]
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
                '<td align="left" class="pt-3-half" contenteditable="false">Definition of the main contacts for all parties</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Definition of roles & responsibilities</td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false"><button type="button" onclick="location.href = ' +
                "'/solution'" +
                '" class="btn btn-warning" style="width: 200px;">Solution Requirements</button></td>',
                '<td align="left" class="pt-3-half" contenteditable="false"><button type="button" onclick="location.href = ' +
                "'/material-list'" +
                '" class="btn btn-warning" style="width: 200px;">Material</button></td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Not applicable in countries where the app is already integrated / released</td>',
                '<td align="left" class="pt-3-half" contenteditable="false"><button type="button" onclick="location.href = ' +
                "'/payment-integration'" +
                '" class="btn btn-warning" style="width: 200px;">Payment Integration</button></td>',
                '<td align="left" class="pt-3-half" contenteditable="false" rowspan="5"><button type="button" onclick="location.href = ' +
                "'/mobile-web-apps'" +
                '" class="btn btn-warning" style="width: 200px; height: 130px; margin-top: 25px;">Mobile & Web Apps</button></td>',
                '', '', '', '',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false" rowspan="4"><button type="button" onclick="location.href = ' +
                "'/master-data-model'" +
                '" class="btn btn-warning" style="width: 200px; height: 100px; margin-top: 20px;">Master Data & Model</button></td>',
                '', '', '',
                '<td align="left" class="pt-3-half" contenteditable="false" rowspan="3"><button type="button" onclick="location.href = ' +
                "'/install-config'" +
                '" class="btn btn-warning" style="width: 200px; height: 80px; margin-top: 15px;">Installation & config</button></td>',
                '', '',
                '<td align="left" class="pt-3-half" contenteditable="false" rowspan="7"><button type="button" onclick="location.href = ' +
                "'/technical-cooler-onboarding'" +
                '" class="btn btn-warning" style="width: 200px; height: 150px; margin-top: 55px;">Cooler Onboarding</button></td>',
                '', '', '', '', '', '',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>'
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

    def post(self, request):
        try:
            current_user = request.user
            post_value = request.POST

            page_name = post_value['page_name']
            owners = post_value['owners']
            status = post_value['status']
            print(page_name, owners, status)
            page_content = PageContents.objects.filter(page_name=page_name)
            if page_content:
                page_content = page_content[0]
                page_content.owners = owners
                page_content.status = status
                page_content.save()
            else:
                PageContents.objects.create(
                    page_name=page_name, owners=owners, status=status)

        except Exception as e:
            return JsonResponse({'status': 400, 'message': str(e)})

        return JsonResponse({'status': 200, 'message': ''})
