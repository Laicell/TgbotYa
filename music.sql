BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "music" (
	"ld"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"file_id"	TEXT NOT NULL,
	"right_answer"	TEXT NOT NULL,
	"wrong_answers"	TEXT NOT NULL
);
INSERT INTO "music" VALUES (1,'AwADAgADAwMAAjYzMUoAAT4f_z5YdPEC','Smash Mouth - All Star','Ed Sheeran - Perfect,Kendrick Lamar - All The Stars,Kodaline - All I Want');
INSERT INTO "music" VALUES (2,'AwADAgADBAMAAjYzMUo1bfq2ddOq_gI','Guns N'' Roses - Paradise City','Metallica - Whiskey In The Jar,The Amity Affliction - Drag The Lake,Muse - Uprising');
INSERT INTO "music" VALUES (3,'AwADAgADWAIAAn62MEr0G7s5WfICygI','Foster The People - Pumped up Kicks','Bag Raiders - Shooting Stars,Stuck In the Sound - Let''s Go,Conan Gray - Crush Culture');
INSERT INTO "music" VALUES (4,'AwADAgADbwMAAhNxMErW40TNY2TckwI','Bring Me The Horizon - Sleepwalking','Architects - Naysayer,Parkway Drive - Prey,SUICIDE SILENCE - Disengage');
INSERT INTO "music" VALUES (5,'AwADAgADcAMAAhNxMEqUJ5IHDWQAAf0C','The XX - Intro','BONES UK - PRETTY WASTE,Lana Del Rey - Born To Die,Brennan Savage - Look At Me Now');
COMMIT;
