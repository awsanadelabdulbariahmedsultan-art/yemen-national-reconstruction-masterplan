import hashlib
import json
import os
import sys
from datetime import datetime


def create_submission_package(
    gov_code,
    grid_id,
    project_title,
    students,
    supervisor,
    uni_name,
    project_files_path,
):
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    payload = f"{gov_code}_{grid_id}_{uni_name}_{timestamp}"
    project_uuid = hashlib.sha256(payload.encode()).hexdigest()[:12].upper()

    metadata = {
        "project_uuid": f"YRUM-{gov_code}-{project_uuid}",
        "architecture_lead": "Eng. Awsan Adel Abdulbari Ahmed Sultan",
        "timestamp_utc": timestamp,
        "governorate": gov_code,
        "grid_id": grid_id,
        "project_title": project_title,
        "university": uni_name,
        "academic_supervisor": supervisor,
        "engineering_team": students,
        "status": "Submitted_Under_Review",
        "archive_ready": True,
    }

    output_dir = f"./deploy_output/{gov_code}/{grid_id}"
    os.makedirs(output_dir, exist_ok=True)

    metadata_file = os.path.join(output_dir, "registry_metadata.json")
    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    print(
        f"[تم الإنجاز بنجاح] تم توثيق وتسجيل المشروع بكود: YRUM-{gov_code}-{project_uuid}"
    )
    print(f"[المسار المحلي الجاهز للسحابة]: {output_dir}")
    return metadata


if __name__ == "__main__":
    create_submission_package(
        gov_code="YE-TZ",
        grid_id="TZ-GRID-04-A",
        project_title="شبكة جسور وأنفاق تقاطع صبر الحضري",
        students=["م. أحمد خالد", "م. سمير علي"],
        supervisor="د. محمد الشميري",
        uni_name="جامعة تعز",
        project_files_path="./drawings",
    )
