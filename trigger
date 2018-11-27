DELIMITER $$
CREATE TRIGGER delete_natural 
    BEFORE DELETE ON satellites_satellite
    FOR EACH ROW 
BEGIN
	DELETE FROM satellites_naturalsatellite where satelliteName_id=old.satelliteName;
END$$
DELIMITER;

CREATE PROCEDURE nearestGalaxy ( in inputdistance decimal(10,5) )
BEGIN
	SELECT galaxyName,distance from galaxy_galaxy where distance <inputdistance;
END