INSERT INTO numbers (number_id)
    VALUES ('0'), ('1'), ('2'), ('3'), ('4'), ('5'), ('6'), ('7'), ('8'), ('9'), ('10'), ('11'),
    ('12'), ('13'), ('14'), ('15'), ('16'), ('17'), ('18'), ('19'), ('20'), ('21'), ('22');

INSERT INTO age_count (day_month_year)
    VALUES ('day'), ('days'), ('week'), ('weeks'), ('month'), ('months'), ('year'), ('years');

INSERT INTO number_age_count (number_id, day_month_year_id)
    VALUES (3, 4), (2, 5), (4, 6), (2, 7), (4, 4), (3, 6), (9, 6), (6, 6), (3, 6), (2, 7);

INSERT INTO animal_type (type_id)
    VALUES ('cat');

INSERT INTO breed (breed_id)
    VALUES ('domestic shorthair'), ('domestic mediumhair'), ('siamese'), ('russian blue'), ('domestic longhair'),
        ('manx'), ('ragdoll'), ('snowshoe/domestic shorthair'), ('snowshoe'), ('angora');

INSERT INTO color (color_id)
    VALUES ('orange'), ('blue'), ('white'), ('black'), ('brown'),
        ('seal'), ('Breed Specific'), ('cream'), ('chocolate'), ('silver'),
        ('blue cream'), ('lynx'), ('red'), ('null');

INSERT INTO outcome_subtype (subtype_id)
    VALUES ('Partner'), ('Offsite'), ('SCRP'), ('Foster'), ('In Kennel'),
        ('Suffering'), ('Rabies Risk'), ('Medical'), ('At Vet'), ('null');

INSERT INTO outcome_type (type_id)
    VALUES ('Transfer'), ('Adoption'), ('Return to Owner'), ('Died'), ('Euthanasia'),
        ('Missing'), ('Disposal'), ('Rto-Adopt');

INSERT INTO outcome_month (month_id)
    VALUES (1), (2), (3), (4), (5), (6), (7), (8), (9), (10), (11), (12);

INSERT INTO outcome_year (year_id)
    VALUES (2013), (2014), (2015), (2016), (2017), (2018);

INSERT INTO cats (age_upon_outcome_id, animal_id, animal_type_id, nickname_id, breed_id,
                  color1_id, color2_id, date_of_birth_id, outcome_subtype_id, outcome_type_id,
                  outcome_month_id, outcome_year_id)
    VALUES (1, 'A684346', 1, '', 1, 1, 14, '2014-07-07 00:00:00', 1, 1, 7, 2),
           (2, 'A685067', 1, 'Lucy', 2, 2, 3, '2014-06-16 00:00:00', 11, 2, 8, 2),
           (3, 'A678580', 1, '*Frida', 3, 3, 4, '2014-03-26 00:00:00', 2, 2, 6, 2),
           (4, 'A675405', 1, 'Stella Luna', 4, 4, 1, '2013-03-27 00:00:00', 3, 3, 3, 2),
           (5, 'A670420', 1, '', 5, 5, 2, '2013-12-16 00:00:00', 4, 1, 1, 2),
           (6, 'A684460', 1, 'Elsa', 6, 5, 6, '2014-06-02 00:00:00', 5, 2, 8, 2),
           (7, 'A673952', 1, '', 7, 6, 5, '2013-07-05 00:00:00', 6, 1, 3, 2),
           (8, 'A686497', 1, 'Chester', 8, 7, 11, '2014-03-22 00:00:00', 7, 2, 8, 2),
           (9, 'A687965', 1, '*Oliver', 9, 2, 12, '2014-08-03 00:00:00', 8, 2, 10, 2),
           (10, 'A668547', 1, '*Preston', 10, 8, 13, '2012-12-04 00:00:00', 9, 1, 12, 1);
