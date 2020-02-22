def gen_organization(id, name, email):
    return {"id": id, "name": name, "email": email}

def gen_campaign(id, name, thumb_url, dest_url):
    return {"id": id, "name": name, "thumb_url": thumb_url, "dest_url": dest_url}

def gen_flyer(id, building_name, floor_num, hits):
    return {"id": id, "building_name": building_name, "floor_num": floor_num, "hits": hits}

def gen_accepted_job(job_id):
    return {"job_id": job_id}

def gen_newly_generated_pdf(download_url):
    return {"download_url": download_url}