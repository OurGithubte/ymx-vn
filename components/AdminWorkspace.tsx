"use client";

import { FormEvent, useMemo, useState } from "react";
import Link from "next/link";
import { Archive, BriefcaseBusiness, CalendarClock, Download, Eye, LogOut, MailCheck, Pencil, Plus, Search, Star, Users, XCircle } from "lucide-react";
import type { Job } from "@/lib/jobs";
import { STATUS_LABELS } from "@/lib/job-schema";
import { useToast } from "./admin/Toast";
import { ConfirmDialog } from "./admin/ConfirmDialog";

type Application = { id:string; job_id:string; job_title:string; full_name:string; email:string; phone:string; experience_years:number|null; status:string; rating:number|null; hr_notes:string|null; created_at:string; cv_path:string };
type Profile = { full_name:string|null; role:string };
const statuses=["new","reviewing","shortlisted","interview","offered","hired","rejected","withdrawn"];

export function AdminWorkspace({profile,jobs:initialJobs,applications:initialApps}:{profile:Profile;jobs:Job[];applications:Application[]}) {
  const [tab,setTab]=useState<"overview"|"jobs"|"candidates">("overview");
  const [jobs,setJobs]=useState(initialJobs); const [apps,setApps]=useState(initialApps);
  const [query,setQuery]=useState(""); const [statusFilter,setStatusFilter]=useState("all"); const [jobFilter,setJobFilter]=useState("all");
  const [selected,setSelected]=useState<Application|null>(null); const [emailTarget,setEmailTarget]=useState<Application|null>(null);
  const [emailType,setEmailType]=useState<"interview"|"offered"|"rejected">("interview");const canManageRecruitment=["admin","hr"].includes(profile.role);
  const [pendingStatus,setPendingStatus]=useState<{job:Job;status:"closed"|"archived"}|null>(null);
  const { notify } = useToast();
  const filtered=useMemo(()=>apps.filter(a=>(statusFilter==="all"||a.status===statusFilter)&&(jobFilter==="all"||a.job_id===jobFilter)&&`${a.full_name} ${a.email} ${a.job_title}`.toLowerCase().includes(query.toLowerCase())),[apps,query,statusFilter,jobFilter]);

  async function updateApplication(id:string,payload:Record<string,unknown>){const response=await fetch(`/api/admin/applications/${id}`,{method:"PATCH",headers:{"content-type":"application/json"},body:JSON.stringify(payload)});const result=await response.json();if(!response.ok){alert(result.error||"Update failed");return false;}setApps(list=>list.map(a=>a.id===id?{...a,...result.application}:a));return true;}
  async function saveReview(event:FormEvent<HTMLFormElement>){event.preventDefault();if(!selected)return;const data=new FormData(event.currentTarget);const rating=String(data.get("rating")||"");const ok=await updateApplication(selected.id,{rating:rating?Number(rating):null,hr_notes:String(data.get("hr_notes")||"")});if(ok)setSelected(null);}
  async function deleteApplication(application:Application){if(!confirm(`Permanently delete ${application.full_name}'s application and CV?`))return;const response=await fetch(`/api/admin/applications/${application.id}`,{method:"DELETE"});const result=await response.json();if(!response.ok){alert(result.error||"Delete failed");return;}setApps(list=>list.filter(item=>item.id!==application.id));setSelected(null);}
  async function sendEmail(event:FormEvent<HTMLFormElement>){event.preventDefault();if(!emailTarget)return;const data=Object.fromEntries(new FormData(event.currentTarget));const response=await fetch(`/api/admin/applications/${emailTarget.id}/email`,{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify(data)});const result=await response.json();if(!response.ok){alert(result.error||"Email could not be sent.");return;}setApps(list=>list.map(app=>app.id===emailTarget.id?{...app,status:result.status}:app));setEmailTarget(null);alert("Email sent and recorded.");}

  async function signOut(){await fetch("/api/admin/logout",{method:"POST"});window.location.href="/admin/login";}

  async function confirmQuickStatus(){
    if(!pendingStatus)return;
    const {job,status}=pendingStatus;
    const response=await fetch(`/api/admin/jobs/${job.id}`,{method:"PATCH",headers:{"content-type":"application/json"},body:JSON.stringify({status})});
    const result=await response.json();
    setPendingStatus(null);
    if(!response.ok){notify(result.error||"Không thể cập nhật tin.","error");return;}
    setJobs(list=>list.map(j=>j.id===job.id?result.job:j));
    notify(status==="closed"?"Đã đóng tin tuyển dụng.":"Đã lưu trữ tin tuyển dụng.","success");
  }

  return <main className="admin-shell">
    <aside><div className="brand"><span className="logo-mark">YMX</span><span><strong>Recruitment</strong><small>{profile.role} workspace</small></span></div><nav><button className={tab==="overview"?"active":""} onClick={()=>setTab("overview")}>Overview</button><button className={tab==="jobs"?"active":""} onClick={()=>setTab("jobs")}>Job postings</button><button className={tab==="candidates"?"active":""} onClick={()=>setTab("candidates")}>Candidates</button></nav></aside>
    <section className="admin-main"><header><div><span className="eyebrow blue">Recruitment operations</span><h1>{profile.full_name?`Hello, ${profile.full_name}`:"HR workspace"}</h1></div><div className="button-row">{canManageRecruitment&&<Link className="button primary" href="/admin/jobs/new"><Plus size={17}/>Create job</Link>}<button className="button" onClick={signOut}><LogOut size={17}/>Sign out</button></div></header>
      {tab==="overview"&&<><div className="metric-grid"><Metric icon={<Users/>} label="New candidates" value={apps.filter(a=>a.status==="new").length} note="Awaiting review"/><Metric icon={<BriefcaseBusiness/>} label="Open jobs" value={jobs.filter(j=>j.status==="published").length} note="Published positions"/><Metric icon={<CalendarClock/>} label="Interviews" value={apps.filter(a=>a.status==="interview").length} note="In interview stage"/><Metric icon={<MailCheck/>} label="Shortlisted" value={apps.filter(a=>a.status==="shortlisted").length} note="Ready for contact"/></div><JobsTable jobs={jobs} canManage={canManageRecruitment} onQuickStatus={(job,status)=>setPendingStatus({job,status})}/></>}
      {tab==="jobs"&&<JobsTable jobs={jobs} canManage={canManageRecruitment} onQuickStatus={(job,status)=>setPendingStatus({job,status})}/>}
      {tab==="candidates"&&<section className="admin-table"><div className="table-heading admin-search"><div><h2>Candidate pipeline</h2><p>Review CVs, record assessment and communicate decisions.</p></div><label><Search size={16}/><input value={query} onChange={e=>setQuery(e.target.value)} placeholder="Search candidate…"/></label></div><div className="pipeline-filters"><select value={statusFilter} onChange={e=>setStatusFilter(e.target.value)}><option value="all">All statuses</option>{statuses.map(s=><option key={s}>{s}</option>)}</select><select value={jobFilter} onChange={e=>setJobFilter(e.target.value)}><option value="all">All positions</option>{jobs.map(j=><option value={j.id} key={j.id}>{j.title.vi}</option>)}</select><span>{filtered.length} candidate(s)</span></div><div className="table-scroll"><table><thead><tr><th>Candidate</th><th>Position</th><th>Rating</th><th>CV</th><th>Status</th><th>Actions</th></tr></thead><tbody>{filtered.map(app=><tr key={app.id}><td><button className="candidate-name" onClick={()=>setSelected(app)}><strong>{app.full_name}</strong><small>{app.email}<br/>{app.phone}</small></button></td><td>{app.job_title}<small>{new Date(app.created_at).toLocaleDateString()}</small></td><td><span className="rating"><Star size={13}/>{app.rating||"—"}</span></td><td><a className="icon-button" aria-label={`Download CV of ${app.full_name}`} href={`/api/admin/applications/${app.id}/cv`} target="_blank"><Download size={16}/></a></td><td><select value={app.status} onChange={e=>updateApplication(app.id,{status:e.target.value})}>{statuses.map(s=><option key={s}>{s}</option>)}</select></td><td><div className="email-actions"><button onClick={()=>setSelected(app)}>Review</button>{canManageRecruitment&&<button onClick={()=>{setEmailType("interview");setEmailTarget(app)}}>Email</button>}</div></td></tr>)}</tbody></table></div></section>}
    </section>
    {selected&&<Modal close={()=>setSelected(null)}><form className="job-modal review-modal" onSubmit={saveReview}><h2>{selected.full_name}</h2><p>{selected.job_title} · {selected.email} · {selected.phone}</p><a className="button" href={`/api/admin/applications/${selected.id}/cv`} target="_blank"><Download size={16}/>Open CV</a><label>Rating<select name="rating" defaultValue={selected.rating||""}><option value="">Not rated</option>{[1,2,3,4,5].map(n=><option key={n} value={n}>{n} / 5</option>)}</select></label><label>Private HR notes<textarea name="hr_notes" rows={7} defaultValue={selected.hr_notes||""} maxLength={5000}/></label><div className="review-actions"><button type="button" className="danger-button" onClick={()=>deleteApplication(selected)}>Delete candidate & CV</button><div className="button-row"><button type="button" className="button" onClick={()=>setSelected(null)}>Cancel</button><button className="button primary">Save review</button></div></div></form></Modal>}
    {emailTarget&&<Modal close={()=>setEmailTarget(null)}><form className="job-modal" onSubmit={sendEmail}><h2>Email {emailTarget.full_name}</h2><label>Template<select name="type" value={emailType} onChange={event=>setEmailType(event.target.value as typeof emailType)}><option value="interview">Interview invitation</option><option value="offered">Successful result</option><option value="rejected">Unsuccessful result</option></select></label><label>Interview date & time{emailType!=="interview"&&" (optional)"}<input name="interviewAt" type="datetime-local" required={emailType==="interview"}/></label><label>Interview location / meeting link{emailType!=="interview"&&" (optional)"}<input name="location" required={emailType==="interview"}/></label><label>Additional note (optional)<textarea name="note" rows={4} maxLength={1000}/></label><div className="button-row"><button type="button" className="button" onClick={()=>setEmailTarget(null)}>Cancel</button><button className="button primary">Send email</button></div></form></Modal>}
    <ConfirmDialog
      open={!!pendingStatus}
      title={pendingStatus?.status==="closed"?"Đóng tin tuyển dụng?":"Lưu trữ tin tuyển dụng?"}
      message={pendingStatus?.status==="closed"?"Tin sẽ ngừng hiển thị công khai và không nhận thêm hồ sơ mới.":"Tin sẽ được chuyển vào lưu trữ và ẩn khỏi danh sách đang tuyển."}
      confirmLabel={pendingStatus?.status==="closed"?"Đóng tin":"Lưu trữ"}
      danger
      onConfirm={confirmQuickStatus}
      onCancel={()=>setPendingStatus(null)}
    />
  </main>;
}

function Metric({icon,label,value,note}:{icon:React.ReactNode;label:string;value:number;note:string}){return <article>{icon}<span>{label}</span><strong>{value}</strong><small>{note}</small></article>}

function JobsTable({jobs,canManage,onQuickStatus}:{jobs:Job[];canManage:boolean;onQuickStatus:(job:Job,status:"closed"|"archived")=>void}){
  return <section className="admin-table">
    <div className="table-heading"><div><h2>Job postings</h2><p>Sửa, xem trước, đóng hoặc lưu trữ tin tuyển dụng.</p></div></div>
    <div className="table-scroll">
      <table>
        <thead><tr><th>Position</th><th>Department</th><th>Location</th><th>Status</th>{canManage&&<th>Actions</th>}</tr></thead>
        <tbody>
          {jobs.map(job=>
            <tr key={job.id}>
              <td><strong>{job.title.vi}</strong></td>
              <td>{job.department}</td>
              <td>{job.location}</td>
              <td><span className={`status ${job.status}`}>{(job.status && STATUS_LABELS[job.status])||job.status}</span></td>
              {canManage&&<td><div className="job-row-actions">
                <Link href={`/admin/jobs/${job.id}/edit`} className="icon-button" aria-label="Sửa" title="Sửa"><Pencil size={15}/></Link>
                <Link href={`/admin/jobs/${job.id}/preview`} className="icon-button" aria-label="Xem trước" title="Xem trước"><Eye size={15}/></Link>
                {job.status==="published"&&<button type="button" className="icon-button" aria-label="Đóng tin" title="Đóng tin" onClick={()=>onQuickStatus(job,"closed")}><XCircle size={15}/></button>}
                {job.status!=="archived"&&<button type="button" className="icon-button" aria-label="Lưu trữ" title="Lưu trữ" onClick={()=>onQuickStatus(job,"archived")}><Archive size={15}/></button>}
              </div></td>}
            </tr>
          )}
        </tbody>
      </table>
    </div>
  </section>;
}

function Modal({children,close}:{children:React.ReactNode;close:()=>void}){return <div className="modal-backdrop" onMouseDown={e=>{if(e.currentTarget===e.target)close()}}><div className="modal-frame"><button className="modal-close" aria-label="Close" onClick={close}><span aria-hidden>×</span></button>{children}</div></div>}
