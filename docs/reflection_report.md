# Reflection & Demo Report

## Challenges Faced
- Fixing the missing `date` column in the Monitoring table that caused 500 errors.
- Ensuring relational integrity and query efficiency by adding foreign keys and indexes.
- Implementing audit trails to track every user action in the backend.

## Lessons Learned
- Proper database design (indexes, foreign keys, and timestamps) is essential for reliability and performance.
- Linking backend actions to audit logs increases transparency and trust for end users.
- Testing APIs thoroughly in Postman helps identify missing fields or logical errors early.

## Backend Impact
- Feed and Monitoring APIs now automatically log all user actions in the `AuditLog` table.
- This audit trail ensures traceability and aligns with SDG 3 by maintaining data integrity and reliability.
- The backend is now more resilient, trustworthy, and ready for real-world adoption.