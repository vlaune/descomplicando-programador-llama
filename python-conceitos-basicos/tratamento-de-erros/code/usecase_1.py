def get_anbima_holidays():
    with db_connection_handler as database:
        try:
            anbima_holidays =(
                database.session
                    .query(AnbimaHolidaysModel)
                    .withentities(AnbimaHolidaysModel.holiday_date)
                    .all()
            )
            return anbima_holidays
        except NoResultFound:
            return None
        except:
            database.session.rollback()
        finally:
            database.session.close()