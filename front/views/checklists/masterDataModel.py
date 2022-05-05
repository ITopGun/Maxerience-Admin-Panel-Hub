from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from front.models import PageContents
import json


class ChecklistsMasterDataModelView(View):
    template_name = 'checklists/master-data-model.html'

    def get(self, request):
        page_name = 'masterDataModel'
        try:
            page_content = PageContents.objects.filter(page_name=page_name)
            if page_content:
                page_content = page_content[0]
                statusInit = json.loads(page_content.status)
                ownerInit = json.loads(page_content.owners)
            else:
                ownerInit = [10, 5, 5, 10, 1, 1, 10, 5, 1, 1, 10, 5, 1]
                statusInit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            id = [
                '1', '1.1', '1.2',
                '2', '2.1', '2.2',
                '3', '3.1', '3.2', '3.3',
                '4', '4.1', '4.2'
            ]
            description = [
                "Master Data & SKUs selection", "&nbsp;SKUs definition", "&nbsp;SKU Purchase & Shipment",
                "Model - Package & Label  Training", "&nbsp;SKUs Training", "&nbsp;Model Deployment",
                "Product MD", "&nbsp;Provide product MD & Pictures", "&nbsp;Import product MD", "&nbsp;Upload MD pictures",
                "Outlet MD", "&nbsp;Provide outlet MD", "&nbsp;Import / create outlet(s)"
            ]
            bold = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
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
                '<td align="left" class="pt-3-half" contenteditable="false">Quantity and definition about the initial SKUs that will be trained</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Skus defined must be purchased and shipped to Maxerience for training and model creation</td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Pre-labelling, labelling, annotation, model training & accuracy fine tune</td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Model will be downloaded to the GPUs</td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Product MD and pictures (thumbnails) must be provided, the images are the ones that will be displayed in the Apps.</td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false"></td>',
                '<td align="left" class="pt-3-half" contenteditable="false">Outlet MD refers to the cooler locations (Name, code, address, etc.).</td>',
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
