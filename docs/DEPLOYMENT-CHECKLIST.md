# Production deployment checklist

## Supabase

- Create the production project in a region close to Vietnam.
- Run `supabase/schema.sql`, then `supabase/seed.sql`.
- Create the first HR user in Authentication.
- Insert that user's UUID into `public.profiles` with role `admin`.
- Confirm the `candidate-cvs` bucket is private and limited to 5 MB.
- Test that anonymous users cannot read `applications`, `profiles` or storage objects.
- Copy project URL, anon key and service role key into Vercel. Never commit the service role key.

## Resend

- Verify the company sending domain.
- Configure SPF and DKIM records.
- Create a restricted production API key.
- Use an address that can receive replies, for example `recruitment@company-domain`.
- Send one test message for each template: receipt, interview, successful result and unsuccessful result.

## Vercel

- Import `OurGithubte/ymx-vn` as a Next.js project.
- Add every variable from `.env.example` to Production and Preview environments.
- Set `NEXT_PUBLIC_SITE_URL` to the final HTTPS domain.
- Deploy and confirm `/vi`, `/en`, `/zh`, `/admin/login`, `/robots.txt` and `/sitemap.xml`.
- Attach the company domain and redirect the old GitHub Pages URL after acceptance testing.

## End-to-end acceptance

- Publish a test job from HR and confirm it appears immediately in all three languages.
- Submit a test PDF CV and receive the confirmation email.
- Confirm HR can search the candidate, open the private CV and save rating/notes.
- Move the candidate through shortlisted and interview states.
- Send an interview invitation with time and location.
- Send a final result and confirm email/status history is recorded.
- Delete the test candidate and CV after acceptance testing.
