-- Migration 0002: extend public.jobs with the MVP recruitment fields used by
-- the new job editor (create / edit / preview / publish / close).
--
-- Scope note: an earlier, more elaborate version of this migration added 18
-- columns (structured salary, education level, industries, keywords, contact
-- routing, etc.). That version was never run against production. It has been
-- replaced by this MVP version — anh Hướng asked to drop the extra fields as
-- unnecessary complexity. Only 5 columns are added now.
--
-- Safe to run multiple times (fully idempotent): every column uses
-- "add column if not exists" with a sensible default, so existing rows
-- (including the two seeded sample jobs, quality-engineer and
-- production-technician) keep working unchanged and simply receive the
-- default value for the new columns. No data is deleted, no column is
-- dropped, no row is touched. RLS is left enabled and untouched — this
-- file contains no "row level security" statement at all; the existing
-- policies in supabase/schema.sql already cover every column of the
-- jobs table (they are not column-scoped), so no policy change is
-- needed or made here.
--
-- How to run: paste this file into the Supabase SQL editor for the
-- project, or `supabase db execute -f supabase/migrations/0002_job_posting_fields.sql`.
-- Do NOT run against production until approved by anh Hướng.
--
-- Deployment order (mandatory — do not skip or reorder):
--   1. Run this migration against the target Supabase project.
--   2. Run the verification queries at the bottom of this file and confirm
--      the 5 new columns exist and the two sample jobs are still present.
--   3. Only then deploy/merge the application code on this branch.
-- Reason: the job-create and job-edit-save API routes write to the new
-- columns below; deploying the code before the migration will make those
-- two actions fail (Postgres "column does not exist"), even though every
-- other page (Careers list/detail, admin dashboard, preview, Đóng tin/Lưu
-- trữ quick actions) keeps working with or without this migration, because
-- those paths only read/write pre-existing columns.

begin;

alter table public.jobs add column if not exists vacancies integer not null default 1;
alter table public.jobs add column if not exists level text;
alter table public.jobs add column if not exists salary_text text;
alter table public.jobs add column if not exists application_deadline date;
alter table public.jobs add column if not exists benefits jsonb not null default '{}'::jsonb;

-- Basic data-integrity guard (guarded so re-running the migration never errors).
do $$ begin
  alter table public.jobs add constraint jobs_vacancies_check check (vacancies >= 1);
exception when duplicate_object then null;
end $$;

commit;


-- =================================================================================
-- VERIFICATION — run these SELECTs manually after applying the migration above.
-- Not part of the transaction; read-only, safe to run any time.
-- =================================================================================

-- 1) Expect exactly 5 rows (one per new column). If fewer come back, the
--    migration did not fully apply — investigate before deploying the code.
-- select column_name, data_type, column_default, is_nullable
-- from information_schema.columns
-- where table_schema = 'public' and table_name = 'jobs'
--   and column_name in ('vacancies','level','salary_text','application_deadline','benefits')
-- order by column_name;

-- 2) Expect exactly 2 rows — confirms the sample jobs survived the migration
--    untouched (id/slug/status unchanged, new columns present with defaults).
-- select id, slug, status, vacancies, level, salary_text, application_deadline
-- from public.jobs
-- where id in ('quality-engineer','production-technician');

-- 3) Expect RLS still "t" (enabled) on jobs, unchanged by this migration.
-- select relrowsecurity from pg_class where relname = 'jobs' and relnamespace = 'public'::regnamespace;

-- 4) Expect exactly 1 row — confirms the vacancies check constraint was created.
-- select conname from pg_constraint where conrelid = 'public.jobs'::regclass and conname = 'jobs_vacancies_check';


-- =================================================================================
-- ROLLBACK — only run this block if migration 0002 needs to be reverted.
-- Uncomment and execute manually; NOT run automatically by this file.
--
-- *** WARNING — READ BEFORE RUNNING ***
-- Dropping these columns is DESTRUCTIVE once real data exists in them: any
-- vacancies/level/salary_text/application_deadline/benefits that staff have
-- entered through the job editor will be permanently lost — this is a plain
-- column drop, not a soft delete, and there is no undo. It does NOT touch
-- id/slug/department/location/employment_type/title/summary/responsibilities/
-- requirements/status/published_at/created_by/created_at/updated_at, so the
-- two sample jobs and the "old shape" of every job row are preserved — but
-- the 5 new columns' content is not.
-- Do NOT run this against production without first taking a full backup
-- (e.g. Supabase dashboard "Database > Backups", or pg_dump of public.jobs)
-- and confirming anh Hướng has approved the rollback.
-- =================================================================================

-- begin;
-- alter table public.jobs drop constraint if exists jobs_vacancies_check;
-- alter table public.jobs drop column if exists vacancies;
-- alter table public.jobs drop column if exists level;
-- alter table public.jobs drop column if exists salary_text;
-- alter table public.jobs drop column if exists application_deadline;
-- alter table public.jobs drop column if exists benefits;
-- commit;
